// =========================
// Live Clock
// =========================

function updateClock() {

    const now = new Date();

    const options = {
        weekday: "short",
        day: "2-digit",
        month: "short",
        year: "numeric"
    };

    const date = now.toLocaleDateString("en-IN", options);
    const time = now.toLocaleTimeString();

    const clock = document.getElementById("clock");

    if (clock) {
        clock.innerHTML = `${date} | ${time}`;
    }
}

setInterval(updateClock, 1000);
updateClock();


// =========================
// Animated Counter
// =========================

const counters = document.querySelectorAll(".card h2");

counters.forEach(counter => {

    const text = counter.innerText.replace(/,/g, "");

    if (!isNaN(text)) {

        const target = parseInt(text);

        let count = 0;

        const speed = Math.ceil(target / 80);

        const timer = setInterval(() => {

            count += speed;

            if (count >= target) {

                count = target;
                clearInterval(timer);

            }

            counter.innerText = count.toLocaleString();

        }, 20);

    }

});