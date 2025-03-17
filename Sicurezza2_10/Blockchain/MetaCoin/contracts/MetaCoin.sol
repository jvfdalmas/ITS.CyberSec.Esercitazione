// SPDX-License-Identifier: MIT
// Tells the Solidity compiler to compile only from v0.8.13 to v0.9.0
pragma solidity ^0.8.13;

import "./ConvertLib.sol";

// This is just a simple example of a coin-like contract.
// It is not ERC20 compatible and cannot be expected to talk to other
// coin/token contracts.


contract MetaCoin {

	//le variabili definite all'interno del contratto sono archiviate
	//nella blockchain

	/*
		Se stessimo parlando di una filiera agroalimentare, allora cosa dovrebbe essere
		archiviato nella blockchain?
		1) ruolo del partecipante (produttore, distributore, negoziante)
		2) id del partecipante
		3) prodotto trasferito da sorgente a destinazione. 
		   Esempio: patate, 100kg, De Cupis, Antonelli. Oppure
		   patate, 20Kg, Antonelli, Marciniewski

		dovremmo quindi definire un mapping tra partecipante e elenco dei prodotti in suo possesso
		Però potremmo anche dire la seguente cosa
		De Cupis produce 100kg di patate e quindi De Cupis assegna a questi 100kg di patate 
		un ID unico (es: IDP011)
		{key: IPD011, valore: {tipo: patata, quantità: 100kg}}

		Forse potremmo avere il partecipante come chiave
		Transazione: de cupis fornisce 100 kg di patate a antonelli
		risultato: k: Antonelli, ruolo: distributore, prodotti:[{patate, 100kg, de cupis}, {fave, 7 kg, krytowski}, ...]

		Transazione: antonelli vende 10 kg di patate prodotte da de cupis a Marciniewsky
		Risultato
			k: Antonelli, ruolo: distributore, prodotti:[{patate, 90kg, de cupis}, {fave, 7 kg, krytowski}, ...]		
			k: Marciniewski, ruolo: negoziante, prodotti:[{patate, 10kg, Antonelli}, {fave, 1 kg, Morjani}, ...]		


		Quando marciniewski vende le patate, allora
		Transazione: marciniewski vende 1kg di patate (lo verifichiamo dallo scontrino)
		Risultato: 
			k: Marciniewski, ruolo: negoziante, prodotti:[{patate, 9kg, Antonelli}, {fave, 1 kg, Morjani}, ...]		

		mapping (address => uint) balances;

	*/
	bytes32 public constant PRODUTTORE = keccak256(abi.encodePacked("produttore"));
	bytes32 public constant DISTRIBUTORE = keccak256(abi.encodePacked("distributore"));
	bytes32 public constant NEGOZIANTE = keccak256(abi.encodePacked("negoziante"));


	struct Prodotto {
		string nome;
		int quantita;
		string produttore;
	}

	//I partecipanti, li indirizziamo per CF
	struct Partecipante {
		string nome;
		string ruolo;
		Prodotto[] prodotti;
	}

	//string è il nome del partecipante
	mapping (string => Partecipante) partecipanti;

	string[] produttori;
	string[] distributori;
	string[] negozianti;

	//event Transfer(address indexed _from, address indexed _to, uint256 _value);

	constructor() {
		//per ora nessuna inizializzazione
	}

	function GetHash(string memory s) public pure returns (bytes32) {
		return keccak256(abi.encodePacked(s));
	}

	//transazione: un produttore fornisce una certa quantità di prodotto a un distributore
	function ProduttoreDistributore(string memory produttore, string memory distributore, string memory prodotto, int quantita) public returns(bool ok) {
		Prodotto memory pr = Prodotto("", 0, "");
		pr.nome = prodotto;
		pr.produttore = produttore;
		pr.quantita = quantita;

		//devo verificare che il distributore sia nei partecipanti
		if (bytes(partecipanti[distributore].nome).length != 0) {
			partecipanti[distributore].prodotti.push(pr);
		} else {
			//se non c'è lo aggiunge
			Partecipante storage par = partecipanti[distributore];
			par.nome = distributore;
			par.ruolo = "distributore";
			par.prodotti.push(pr);
		}
		return true;
	}

	function GetProdottiFromDistributore(string memory nomeDistributore) public view returns (Prodotto[] memory) {
		return partecipanti[nomeDistributore].prodotti;
	}

	//transazione: un distributore fornisce una certa quantità di prodotto a un negoziante
	function DistributoreNegoziante(string memory distributore, string memory negoziante, string memory prodotto, int quantita) public returns(bool ok) {

		//devo verificare che il distributore sia nei partecipanti
		if (bytes(partecipanti[distributore].nome).length == 0) {
			return false;
		}

        string memory sRuolo = partecipanti[distributore].ruolo;
		if (GetHash(sRuolo) != DISTRIBUTORE) {
			return false;
		}

		//devo verificare che il distributore abbia il prodotto
		Prodotto[] memory prodotti = partecipanti[distributore].prodotti;
		bool trovato = false;
		for (uint i = 0; i < prodotti.length; i++) {
			if (GetHash(prodotto) == GetHash(prodotti[i].nome)) {
				trovato = true;
				if (prodotti[i].quantita < quantita) {
					return false;
				}
				prodotti[i].quantita -= quantita;
				break;
			}
		}
		if (!trovato) {
			return false;
		}

		// Se il negoziante è già presente, allora aggiungo il
		// prodotto, altrimenti creo anche il negoziante
		if (bytes(partecipanti[negoziante].nome).length == 0) {
			//se non c'è crea il negoziante e poi aggiunge il prodotto
			partecipanti[negoziante].nome = negoziante;
			partecipanti[negoziante].ruolo = "negoziante";
		}

		//qui sono certo che il negoziante esiste
		Partecipante storage par = partecipanti[negoziante];
		Prodotto memory pr = Prodotto("", 0, "");
		pr.nome = prodotto;
		pr.produttore = distributore;
		pr.quantita = quantita;
		par.prodotti.push(pr);
		return true;
	}

	function ElencaProdottiNegoziante(string memory negoziante) public view returns (Prodotto[] memory) {
		return partecipanti[negoziante].prodotti;
	}

	function ElencaProdottoNegoziante(string memory negoziante, string memory nomeProdotto) public view returns (Prodotto[] memory) {
		//in questo caso devo cercare il prodotto
		Prodotto[] memory prodotti = partecipanti[negoziante].prodotti;
		uint conta=0;
		for (uint i = 0; i < prodotti.length; i++) {
			if (GetHash(prodotti[i].nome) == GetHash(nomeProdotto)) {
				conta++;
			}
		}
		Prodotto[] memory prodottiFiltrati = new Prodotto[](conta);
		uint idx=0;
		for (uint i = 0; i < prodotti.length; i++) {
			if (GetHash(prodotti[i].nome) == GetHash(nomeProdotto)) {
				prodottiFiltrati[idx++] = prodotti[i];
			}
		}
		return prodottiFiltrati;
	}







	// function sendCoin(address receiver, uint amount) public returns(bool sufficient) {
	// 	if (balances[msg.sender] < amount) return false;
	// 	balances[msg.sender] -= amount;
	// 	balances[receiver] += amount;
	// 	emit Transfer(msg.sender, receiver, amount);
	// 	return true;
	// }

	// function getBalanceInEth(address addr) public view returns(uint){
	// 	return ConvertLib.convert(getBalance(addr),2);
	// }

	// function getBalance(address addr) public view returns(uint) {
	// 	return balances[addr];
	// }
}
