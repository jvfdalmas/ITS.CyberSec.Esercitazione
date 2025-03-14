import Web3 from 'web3';

//Questa transazione non è attinente ai Metacoin ma è attinente agli ethereum

// Variables definition
const privKey =
  "0xb94d5d0de865367a4fb042df2f808ce7a53b46ec91e9717bd73192397996bacb";

const addressFrom = "0xFF5B8a64f53A0fDFa494cEdb9C91B7E9d25CC501";
const addressTo = "0x52467FfA5c9C76f8e86fB92F1F52E69378EBc61e";

//const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:7545'));

//const web3 = new Web3(new Web3.providers.HttpProvider('http://127.0.0.1:7545'));
const web3 = new Web3("http://127.0.0.1:7545/"); // Ganache;

// Create transaction
const deploy = async () => {
  try {
    console.log(
      `Attempting to make transaction from ${addressFrom} to ${addressTo}`
    );

    const transactionObject = {
      from: addressFrom,
      to: addressTo,
      value: web3.utils.toWei("1", "ether"),
    };

    // Estimate gas
    const gasEstimate = await web3.eth.estimateGas(transactionObject);

    // Add gas to transaction object
    transactionObject.gas = gasEstimate;

    // EIP-1559 gas parameters (adjust values as needed)
    const maxPriorityFeePerGas = web3.utils.toWei('1', 'gwei'); // Example value
    const maxFeePerGas = web3.utils.toWei('2', 'gwei'); // Example value

    transactionObject.maxPriorityFeePerGas = maxPriorityFeePerGas;
    transactionObject.maxFeePerGas = maxFeePerGas;
    

    const createTransaction = await web3.eth.accounts.signTransaction(
      transactionObject,
      privKey
    );

    // Deploy transaction
    const createReceipt = await web3.eth.sendSignedTransaction(
      createTransaction.rawTransaction
    );
    console.log(
      `Transaction successful with hash: ${createReceipt.transactionHash}`
    );
  } catch  (error) {
    console.error("Error during deployment:", error);
  }
};

deploy();

/* From truffle console */
/*
const privKey = "0x7ce93f8606bbdb6358ed39a138001c4aee8ef08ea20955497007f62f97ca0aac"

const addressFrom = '0xD586D7346f3da5D48B76FD6053f992Ca796aB6A5'
const addressTo = '0xF8D24Ac5546C3279C04596adf58AB538C573Fb4F'
const createTransaction = await web3.eth.accounts.signTransaction({"from": addressFrom,"to": addressTo,"value": web3.utils.toWei('1', 'ether'),"gas": '21000',},privKey)
const createReceipt = await web3.eth.sendSignedTransaction(createTransaction.rawTransaction)
createReceipt.transactionHash
*/
