criaCartao(
    'História',
    'Quem descobriu o Brasil?',
    'Pedro Álvares Cabral.'
)

function criaCartao(nome, email , telefone){
    let container = document.getElementById('container');
    let cartao = document.createElement('article');
    cartao.className = 'cartao' ;
    cartao.innerHTML = `
    <div class="conteudo-cartao">
    <h3>${nome}</h3>
    <div class="pergunta-cartao">
        <p>${email}</p>
    </div>
<div class="resposta-cartao">
      <p>${telefone}</p>
</div>
</div>
    `
    let respostaEstaVisivel = false ;
    function viraCartao(){
        respostaEstaVisivel = !respostaEstaVisivel;
        cartao.classList.toggle('active',respostaEstaVisivel);
    }
    cartao.addEventListener('click', viraCartao);



    container.appendChild(cartao)
}