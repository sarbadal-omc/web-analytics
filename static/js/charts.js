async function main() {
    fetchAndRenderTrendChart('trendChart');
    fetchAndRenderFunnelChart('funnelChart');
}

async function getTrendData(url) {
    try {
        const resp = await fetch(url, { method: 'GET' });
        if (!resp.ok) throw new Error('Network response was not ok: ' + resp.status);
        return resp.json();
    } catch (err) {
        console.error('Failed to fetch data from ' + url, err);
        return null;
    }
}

async function getFunnelData(url) {
    try {
        const resp = await fetch(url, { method: 'GET' });
        if (!resp.ok) throw new Error('Network response was not ok: ' + resp.status);
        return resp.json();
    } catch (err) {
        console.error('Failed to fetch data from ' + url, err);
        return null;
    }
}

async function fetchAndRenderTrendChart(containerId) {
    try {
        const data = await getTrendData('/api/data/get-trend-data');
        renderTrendChart(containerId, data.data);
    } catch (err) {
        console.error('Failed to fetch sentiment by region data:', err);
    }
}

async function fetchAndRenderFunnelChart(containerId) {
    try {
        const data = await getFunnelData('/api/data/get-funnel-data');
        renderFunnelChart(containerId, data.data);
    } catch (err) {
        console.error('Failed to fetch sentiment by region data:', err);
    }
}

async function renderTrendChart(containerId, chartData) {
    const trendCtx = document.getElementById(containerId).getContext('2d');
    new Chart(trendCtx, {
        type: 'line',
        data: {
            labels: chartData.labels,
            datasets: [{
                label: 'Visitors',
                data: chartData.data,
                borderColor: '#667eea',
                backgroundColor: 'rgba(102, 126, 234, 0.1)',
                borderWidth: 3,
                fill: true,
                tension: 0.4,
                pointRadius: 6,
                pointBackgroundColor: '#667eea',
                pointBorderColor: '#fff',
                pointBorderWidth: 2
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 35000
                }
            }
        }
    });
}

async function renderFunnelChart(containerId, chartData) {
    const funnelCtx = document.getElementById(containerId).getContext('2d');
    new Chart(funnelCtx, {
        type: 'bar',
        data: {
            labels: chartData.labels,
            datasets: [{
                label: 'Users',
                data: chartData.data,
                backgroundColor: [
                    '#667eea',
                    '#764ba2',
                    '#5a5fc9',
                    '#3498db',
                    '#27ae60'
                ]
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    beginAtZero: true
                }
            }
        }
    });

}
