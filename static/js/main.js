document.addEventListener("DOMContentLoaded", () => {
  // Selected gift state
  let selectedGift = null;
  const guestNameInput = document.getElementById("guest-name");
  const confirmationHeader = document.getElementById("confirmation-header");
  const selectedGiftName = document.getElementById("selected-gift-name");
  const selectedFor = document.getElementById("selected-for");
  const confirmBtn = document.getElementById("confirm-reservation");
  const formGiftId = document.getElementById("form-gift-id");
  const reservationForm = document.getElementById("reservation-form");
  const confirmationModal = document.getElementById("confirmation-modal");
  const modalGiftName = document.getElementById("modal-gift-name");
  const modalGuestName = document.getElementById("modal-guest-name");
  const finalConfirmBtn = document.getElementById("final-confirm");
  const cancelBtn = document.getElementById("cancel-reservation");

  // Initialize GSAP animations
  const tl = gsap.timeline({ delay: 0.3 });

  // Header animation
  tl.from(".animated-header-item", {
    duration: 0.8,
    y: 20,
    opacity: 0,
    stagger: 0.2,
    ease: "power3.out",
  });

  // Form input animation
  tl.from(
    ".animated-form-item",
    {
      duration: 0.8,
      y: 20,
      opacity: 0,
      ease: "power3.out",
    },
    "-=0.4"
  );

  // Gift card animation
  tl.from(
    ".gift-card",
    {
      duration: 0.8,
      y: 50,
      opacity: 1,
      stagger: 0.1,
      ease: "back.out(1.7)",
    },
    "-=0.6"
  );

  // Name input listener
  guestNameInput.addEventListener("input", updateConfirmationHeader);

  // Confirm button shows modal
  confirmBtn.addEventListener("click", () => {
    const name = guestNameInput.value.trim();
    const giftName = selectedGift.querySelector("h3").textContent.trim();

    modalGiftName.textContent = giftName;
    modalGuestName.textContent = name;
    confirmationModal.classList.remove("hidden");
  });

  // Final confirmation
  finalConfirmBtn.addEventListener("click", () => {
    reservationForm.submit();
  });

  // Cancel reservation
  cancelBtn.addEventListener("click", () => {
    confirmationModal.classList.add("hidden");
  });

  // Update the updateConfirmationHeader function
  function updateConfirmationHeader() {
    const name = guestNameInput.value.trim();
    const instructions = document.getElementById("selection-instructions");

    if (selectedGift && name) {
      // Valid selection
      selectedFor.textContent = `For: ${name}`;
      confirmBtn.disabled = false;
      confirmBtn.classList.remove("confirm-disabled");
      confirmBtn.classList.add("confirm-enabled");
      instructions.classList.add("hidden");
    } else {
      // Invalid selection
      selectedFor.textContent = "";
      confirmBtn.disabled = true;
      confirmBtn.classList.remove("confirm-enabled");
      confirmBtn.classList.add("confirm-disabled");

      if (!selectedGift && !name) {
        instructions.textContent = "Please select a gift and enter your name";
      } else if (!selectedGift) {
        instructions.textContent = "Please select a gift";
      } else {
        instructions.textContent = "Please enter your name";
      }
      instructions.classList.remove("hidden");
    }
  }

  // Update the gift selection event listener
  document.querySelectorAll(".select-gift").forEach((button) => {
    button.addEventListener("click", function () {
      const card = this.closest(".gift-card");
      const giftId = card.dataset.giftId;
      const giftName = card.querySelector("h3").textContent.trim();

      // Clear previous selection
      if (selectedGift) {
        selectedGift.classList.remove("selected-card");
        gsap.to(selectedGift, {
          borderWidth: 0,
          boxShadow:
            "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
          duration: 0.3,
        });
      }

      // Set new selection
      selectedGift = card;
      formGiftId.value = giftId;
      selectedGiftName.textContent = giftName;

      // Animate selection
      gsap.fromTo(
        selectedGift,
        {
          borderWidth: 0,
          boxShadow:
            "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        },
        {
          borderWidth: 3,
          boxShadow: "0 0 0 3px rgba(59, 130, 246, 0.3)",
          duration: 0.3,
        }
      );
      selectedGift.classList.add("selected-card");

      // Show confirmation header
      confirmationHeader.classList.remove("hidden");
      updateConfirmationHeader();
    });
  });

  // Confetti setup (keep your existing confetti code)
  const canvas = document.getElementById("confetti-canvas");
  const ctx = canvas.getContext("2d");
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  const confettiPieces = [];
  const colors = ["#ec4899", "#3b82f6", "#f43f5e", "#8b5cf6", "#10b981"];

  class Confetti {
    constructor() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height - canvas.height;
      this.size = Math.random() * 10 + 5;
      this.color = colors[Math.floor(Math.random() * colors.length)];
      this.rotation = Math.random() * 360;
      this.speed = Math.random() * 3 + 2;
      this.rotationSpeed = Math.random() * 5 - 2.5;
      this.oscillation = Math.random() * 2;
      this.oscillationSpeed = Math.random() * 0.1;
      this.time = 0;
    }

    update() {
      this.time += 0.01;
      this.y += this.speed;
      this.rotation += this.rotationSpeed;
      this.x += Math.sin(this.time * this.oscillationSpeed) * this.oscillation;

      if (this.y > canvas.height) {
        this.y = 0;
        this.x = Math.random() * canvas.width;
      }
    }

    draw() {
      ctx.save();
      ctx.translate(this.x, this.y);
      ctx.rotate((this.rotation * Math.PI) / 180);
      ctx.fillStyle = this.color;
      ctx.fillRect(-this.size / 2, -this.size / 2, this.size, this.size);
      ctx.restore();
    }
  }

  for (let i = 0; i < 100; i++) {
    confettiPieces.push(new Confetti());
  }

  function animateConfetti() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    confettiPieces.forEach((confetti) => {
      confetti.update();
      confetti.draw();
    });
    requestAnimationFrame(animateConfetti);
  }
  animateConfetti();

  window.addEventListener("resize", () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  });

  // Flash message animation
  const flashMessages = document.querySelectorAll(".flash-message");
  flashMessages.forEach((msg) => {
    gsap.from(msg, {
      duration: 0.5,
      y: -20,
      opacity: 0,
      ease: "back.out(1.7)",
    });

    setTimeout(() => {
      gsap.to(msg, {
        duration: 0.5,
        opacity: 0,
        y: -20,
        onComplete: () => msg.remove(),
      });
    }, 5000);
  });
});
