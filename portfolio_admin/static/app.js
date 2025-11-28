function carregarConteudo(conteudo) {
    document.querySelectorAll('[id^="content-"]').forEach(element => {
        element.style.display = 'none';
    });
    document.getElementById(`content-${conteudo}`).style.display = 'block';
}

function removerConteudo(){
    document.querySelectorAll('[id^="content-"]').forEach(element => {
        element.style.display = 'none';
    });
}

async function baixarPDF() {
    var nomeArquivo = $.ajax({
        url: '/localizar_curriculo/',
        method: 'GET',
        async: false,
        success: function(response) {
            return response;
        },
        error: function(error) {
            console.error('Erro:', error);
        }
    });

    var caminhoPDF = `${nomeArquivo.responseJSON.path}`;

    var link = document.createElement('a');
    link.href = caminhoPDF;
    link.target = '_blank';
    link.download = '';
    link.click();
}
