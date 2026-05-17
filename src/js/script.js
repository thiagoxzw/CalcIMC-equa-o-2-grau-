// Menu ativo conforme página atual
const links = document.querySelectorAll('nav ul li a');
links.forEach(link => {
  if (link.href === window.location.href) {
    link.style.color = '#00e5ff';
    link.style.fontWeight = 'bold';
  }
});

// Formulário de contato
const form = document.querySelector('.form-contato');
if (form) {
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    alert('Mensagem enviada com sucesso! Entraremos em contato em breve.');
    form.reset();
  });
}
