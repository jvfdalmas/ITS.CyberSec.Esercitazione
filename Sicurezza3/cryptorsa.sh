if [ "$1" == "1" ]
then
    echo "Commando crypta file lungo"
    # Genera una password casuale (32 byte) e la salva in 'password.dat'
    openssl rand -out password.dat 32
    # Esegue la crittografia del file passato come secondo parametro ($2)
    openssl enc -e -in $2 -out $2.enc -kfile password.dat -aes256    
    # Esegue la crittografia del file 'password.dat' usando la chiave pubblica ($3)
    openssl pkeyutl -encrypt -inkey $3 -pubin -in password.dat -out password.dat.enc    
    # Comprimi i file crittografati in un file zip
    zip $2.zip $2.enc password.dat.enc
    # Rimuove i file temporanei
    rm $2.enc $2 password.dat.enc password.dat 
fi

if [ "$1" == "2" ]
then
    echo "Commando decrypta file lungo"
    # Estrai i file dall'archivio zip specificato ($2)
    unzip $2
    # Rimuove l'estensione .zip dal nome del file per ottenere il nome base
    nome="$2"
    fileName=${nome%.*}
    # Decrittografa il file 'password.dat.enc' usando la chiave privata ($3)
    openssl pkeyutl -decrypt -inkey $3 -in password.dat.enc -out password.dat    
    # Usa la password decrittografata in 'password.dat' per decrittografare il file
    openssl enc -d -in $fileName.enc -out $fileName -kfile password.dat -aes256    
    # Rimuove i file temporanei
    rm password.dat.enc password.dat $2 $fileName.enc   
fi
