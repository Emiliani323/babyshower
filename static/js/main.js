        document.addEventListener('DOMContentLoaded', () => {
            // GSAP Animations
            gsap.from(".gift-card", {
                duration: 0.8,
                y: 50,
                opacity: 0,
                stagger: 0.1,
                ease: "back.out(1.7)",
                delay: 0.5
            });

            // Hover animations
            document.querySelectorAll('.gift-card').forEach(card => {
                card.addEventListener('mouseenter', () => {
                    gsap.to(card, {
                        duration: 0.3,
                        scale: 1.03,
                        boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
                        ease: "power2.out"
                    });
                });
                
                card.addEventListener('mouseleave', () => {
                    gsap.to(card, {
                        duration: 0.3,
                        scale: 1,
                        boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
                        ease: "power2.out"
                    });
                });
            });

            // Confetti setup
            const canvas = document.getElementById('confetti-canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            const confettiPieces = [];
            const colors = ['#ec4899', '#3b82f6', '#f43f5e', '#8b5cf6', '#10b981'];

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
                    ctx.rotate(this.rotation * Math.PI / 180);
                    ctx.fillStyle = this.color;
                    ctx.fillRect(-this.size/2, -this.size/2, this.size, this.size);
                    ctx.restore();
                }
            }

            // Create confetti
            for (let i = 0; i < 100; i++) {
                confettiPieces.push(new Confetti());
            }

            function animateConfetti() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                confettiPieces.forEach(confetti => {
                    confetti.update();
                    confetti.draw();
                });
                
                requestAnimationFrame(animateConfetti);
            }

            animateConfetti();

            // Window resize handler
            window.addEventListener('resize', () => {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            });

            // Flash message animation
            const flashMessages = document.querySelectorAll('.flash-message');
            flashMessages.forEach(msg => {
                gsap.from(msg, {
                    duration: 0.5,
                    y: -20,
                    opacity: 0,
                    ease: "back.out(1.7)"
                });

                setTimeout(() => {
                    gsap.to(msg, {
                        duration: 0.5,
                        opacity: 0,
                        y: -20,
                        onComplete: () => msg.remove()
                    });
                }, 5000);
            });
        });