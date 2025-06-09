document.addEventListener('DOMContentLoaded', () => {
    // Header animation
    gsap.from("#header", {
        duration: 1,
        y: -50,
        opacity: 0,
        ease: "back.out(1.7)"
    });

    // Gift cards animation
    gsap.from(".gift-card", {
        duration: 0.8,
        y: 50,
        opacity: 0,
        stagger: 0.1,
        ease: "power2.out",
        delay: 0.3
    });

    // Button hover effects
    document.querySelectorAll('.reserve-btn').forEach(btn => {
        btn.addEventListener('mouseenter', () => {
            gsap.to(btn, {
                duration: 0.2,
                scale: 1.05,
                ease: "power2.out"
            });
        });
        btn.addEventListener('mouseleave', () => {
            gsap.to(btn, {
                duration: 0.2,
                scale: 1,
                ease: "power2.out"
            });
        });
    });

    // Flash messages animation
    document.querySelectorAll('.flash-message').forEach(msg => {
        gsap.from(msg, {
            duration: 0.5,
            x: -50,
            opacity: 0,
            ease: "power2.out"
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