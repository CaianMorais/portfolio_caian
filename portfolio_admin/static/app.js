function carregarConteudo(conteudo) {
    document.querySelectorAll('[id^="content-"]').forEach(element => {
        element.style.display = 'none';
    });
    document.getElementById(`content-${conteudo}`).style.display = 'block';
}

function baixarPDF() {
    var caminhoPDF = "/midia/caian.pdf"; 

    var link = document.createElement('a');
    link.href = caminhoPDF;
    link.target = '_blank';
    link.download = 'caian.pdf';

    link.click();
}
