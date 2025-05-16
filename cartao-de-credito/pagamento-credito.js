
function toggleVisibilidade(icon) {
    const input = icon.previousElementSibling;
  
    if (input.type === "password") {
      input.type = "text";
      icon.classList.remove("bi-eye-fill");
      icon.classList.add("bi-eye-slash-fill");
    } else {
      input.type = "password";
      icon.classList.remove("bi-eye-slash-fill");
      icon.classList.add("bi-eye-fill");
    }
  }
  

 // Seleciona todos os inputs de parcela
 const radios = document.querySelectorAll('input[name="parcela"]');
 const infoPagamento = document.getElementById('info-pagamento');
 const textoParcelamento = document.getElementById('parcelamento-escolhido');
 
 radios.forEach(radio => {
   radio.addEventListener('change', () => {
     const texto = radio.parentElement.textContent.trim();
     textoParcelamento.textContent = `Parcelamento escolhido: ${texto}`;
     infoPagamento.style.display = 'block';
   });
 });
 document.addEventListener('DOMContentLoaded', function () {
  const botaoPagamento = document.querySelector('.btn-pagamento');
  const popup = document.getElementById('popupPagamento');

  if (botaoPagamento) {
    botaoPagamento.addEventListener('click', function () {
      popup.style.display = 'flex';
    });
  }
});
 
document.addEventListener('DOMContentLoaded', function () {
  const botaoPagamento = document.querySelector('.btn-pagamento');
  const popup = document.getElementById('popupPagamento');

  if (botaoPagamento && popup) {
    botaoPagamento.addEventListener('click', function () {
      popup.style.display = 'flex';
    });
  }
});


  






