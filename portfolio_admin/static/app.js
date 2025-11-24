function carregarConteudo(conteudo) {
    // Esconde todos os conteúdos
    document.querySelectorAll('[id^="content-"]').forEach(element => {
        element.style.display = 'none';
    });
    // Mostra o conteúdo específico
    document.getElementById(`content-${conteudo}`).style.display = 'block';
}

function baixarPDF() {
    // Caminho para o arquivo PDF
    var caminhoPDF = "/midia/caian.pdf"; // Substitua pelo caminho real do seu arquivo PDF

    // Cria um link temporário
    var link = document.createElement('a');
    link.href = caminhoPDF;
    link.target = '_blank'; // Abre o link em uma nova aba
    link.download = 'caian.pdf'; // Nome do arquivo para download

    // Simula o clique no link para iniciar o download
    link.click();
}
