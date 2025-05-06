// modern.js - Script pour les animations et comportements du site

document.addEventListener('DOMContentLoaded', function() {
  // Variables
  const header = document.querySelector('.header');
  const navbarToggler = document.querySelector('.navbar-toggler');
  const navbarNav = document.querySelector('.navbar-nav');
  const expertiseText = document.getElementById('text');
  
  // Effet de scroll sur le header
  window.addEventListener('scroll', function() {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });
  
  // Menu mobile toggle amélioré
  if (navbarToggler) {
    navbarToggler.addEventListener('click', function() {
      navbarNav.classList.toggle('active');
      // Ajoute/enlève une classe sur le body pour empêcher le défilement quand le menu est ouvert
      document.body.classList.toggle('menu-open');
    });
    
    // Fermer le menu quand on clique sur un lien
    document.querySelectorAll('.navbar-nav .navbar-link').forEach(link => {
      link.addEventListener('click', function() {
        if (window.innerWidth <= 768) {
          navbarNav.classList.remove('active');
          document.body.classList.remove('menu-open');
        }
      });
    });
    
    // Fermer le menu quand on clique en dehors
    document.addEventListener('click', function(event) {
      if (window.innerWidth <= 768 && 
          !event.target.closest('.navbar-nav') && 
          !event.target.closest('.navbar-toggler') &&
          navbarNav.classList.contains('active')) {
        navbarNav.classList.remove('active');
        document.body.classList.remove('menu-open');
      }
    });
  }
  
  // Texte d'expertise en rotation
  if (expertiseText) {
    const expertises = [
      "Data Analysis",
      "Web Development",
      "Energétique",
      "Python Programming"
    ];
    
    let currentIndex = 0;
    
    function typeText(text, element) {
      element.classList.add('typing-text');
      let i = 0;
      element.textContent = '';
      
      function typing() {
        if (i < text.length) {
          element.textContent += text.charAt(i);
          i++;
          setTimeout(typing, 100);
        } else {
          setTimeout(deleteText, 1500);
        }
      }
      
      function deleteText() {
        if (element.textContent.length > 0) {
          element.textContent = element.textContent.slice(0, -1);
          setTimeout(deleteText, 50);
        } else {
          currentIndex = (currentIndex + 1) % expertises.length;
          setTimeout(() => typeText(expertises[currentIndex], element), 500);
        }
      }
      
      typing();
    }
    
    typeText(expertises[currentIndex], expertiseText);
  }
  
  // Réinitialisation des animations AOS lors des transitions de page
  document.addEventListener('swup:contentReplaced', function() {
    AOS.refresh();
    
    // Réinitialiser le menu mobile à chaque navigation
    if (navbarNav && navbarNav.classList.contains('active')) {
      navbarNav.classList.remove('active');
    }
    
    // Réinitialiser l'animation de texte si on revient à la page d'accueil
    const newExpertiseText = document.getElementById('text');
    if (newExpertiseText && window.typeTextAnimation) {
      window.typeTextAnimation.restart();
    }
  });
  
  // Animation de surbrillance pour les liens actifs
  const currentPath = window.location.pathname;
  document.querySelectorAll('.navbar-link').forEach(link => {
    if (link.getAttribute('href') === currentPath || 
        (currentPath === '/' && link.getAttribute('href') === '/')) {
      link.classList.add('active');
    }
  });
  
  // Animation de chargement de la page
  setTimeout(function() {
    document.body.classList.add('loaded');
  }, 100);
  
  // Initialisation des animations au scroll si elles ne sont pas déjà initialisées
  if (typeof AOS !== 'undefined') {
    AOS.init({
      duration: 800,
      easing: 'ease-out',
      once: false, // Si true, l'animation ne s'applique qu'une seule fois
      mirror: true // Permet aux animations de se déclencher à nouveau lorsqu'on remonte la page
    });
  }
  
  // Interaction avec les cartes de projet/article
  document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('mouseenter', function() {
      this.querySelector('.card-img img')?.classList.add('hovered');
    });
    
    card.addEventListener('mouseleave', function() {
      this.querySelector('.card-img img')?.classList.remove('hovered');
    });
  });
  
  // Gestion de la classe active des liens de navbar
  document.querySelectorAll('.navbar-link').forEach(link => {
    link.addEventListener('click', function() {
      document.querySelectorAll('.navbar-link').forEach(l => l.classList.remove('active'));
      this.classList.add('active');
    });
  });
}); 