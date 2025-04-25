const links = Array.from(document.querySelectorAll('a'));
const pdfLinks = links
  .filter(link => link.href.toLowerCase().endsWith('.pdf'))
  .map(link => ({
    title: link.textContent.trim() || 'sem_titulo',
    url: link.href
  }));

console.log(pdfLinks);

// Se quiser copiar direto como texto
console.log(
  pdfLinks.map(l => `${l.title} - ${l.url}`).join('\n')
);