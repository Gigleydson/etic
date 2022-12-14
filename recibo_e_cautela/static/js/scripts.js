function gerarPDF(){
    const item = document.querySelector(".block-pdf");

    var opt = {
        margin: 0.5,
        filename: "recibo.pdf",
        jsPDF: { unit: "in", format:'a4', orientation: "p" },
    };

    html2pdf().set(opt).from(item).save();
}