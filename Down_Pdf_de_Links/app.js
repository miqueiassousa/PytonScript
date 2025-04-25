// Script JavaScript para pegar todos os links de PDF de uma pagina web

// Encontrar todos os links na página
const links = document.querySelectorAll('a');

// Criar um array para armazenar os links de PDF
const linksPdf = [];

// Iterar sobre todos os links
links.forEach(link => {
    const href = link.getAttribute('href');
    if (href && href.toLowerCase().endsWith('.pdf')) {
        linksPdf.push(href);
    }
});

// Exibir os links de PDF encontrados
if (linksPdf.length > 0) {
    console.log("Links de PDF encontrados:");
    linksPdf.forEach(link => {
        console.log(link);
    });
} else {
    console.log("Nenhum link de PDF encontrado.");
}
