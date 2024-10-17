import * as bootstrap from "bootstrap";

const btnLoadData: HTMLButtonElement | null = document.getElementById('btnLoadData') as HTMLButtonElement;

// senza async await
if (btnLoadData != null){
    btnLoadData.addEventListener('click', ()=>{
        console.log('Bottono cliccato');
        fetch('https://jsonplaceholder.typicode.com/posts?userId=1')
            .then((response)=>response.json())
            .then((valoreDiRisposta: any[])=>{
                console.log(valoreDiRisposta)});
    });
}