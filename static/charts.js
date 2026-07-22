document.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('analyticsChart');

    if (ctx) {
        // Destroy existing chart instance if one already exists to prevent canvas reuse errors
        const existingChart = Chart.getChart(ctx);
        if (existingChart) {
            existingChart.destroy();
        }

        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                datasets: [{
                    label: 'Crowd Analysis',
                    data: [120, 220, 180, 260, 310, 280, 350],
                    borderColor: '#00E5FF',
                    backgroundColor: '#00E5FF',
                    pointBackgroundColor: '#00E5FF',
                    pointRadius: 4,
                    pointHoverRadius: 6,
                    borderWidth: 3,
                    fill: false,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        labels: {
                            color: '#ffffff',
                            font: {
                                size: 14
                            }
                        }
                    }
                },
                scales: {
                    x: {
                        ticks: {
                            color: '#ffffff'
                        },
                        grid: {
                            color: 'rgba(255, 255, 255, 0.08)'
                        }
                    },
                    y: {
                        ticks: {
                            color: '#ffffff'
                        },
                        grid: {
                            color: 'rgba(255, 255, 255, 0.08)'
                        }
                    }
                }
            }
        });
    }
});