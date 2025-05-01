<script>
    let nextService = {
        date: 'Sunday, May 12',
        time: '10:30am',
        address: '456 Church St, Sanctuary'
    };
    let events = [
        { name: 'Youth Group', date: 'Wed, May 15', time: '6:00pm' },
        { name: 'Choir Practice', date: 'Thu, May 16', time: '7:00pm' },
        { name: 'Community Potluck', date: 'Sun, May 19', time: '12:00pm' }
    ];
</script>

<style>
    :root {
        --primary-green: #2d5a27;
        --light-green: #3a7a33;
        --card-bg: #fff;
        --card-shadow: 0 4px 12px rgba(43, 43, 43, 0.1);
        --border-radius: 12px;
        --text-main: #2d2d2d;
        --text-muted: #666;
    }

    .banner {
        background: linear-gradient(90deg, var(--primary-green), var(--light-green));
        color: #fff;
        border-radius: var(--border-radius);
        padding: 1.5rem 2rem;
        margin: 2rem auto 1.5rem auto;
        max-width: 700px;
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        box-shadow: 0 2px 8px rgba(45, 90, 39, 0.15);
    }
    .card {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        padding: 2rem;
        margin: 0 auto 2rem auto;
        max-width: 700px;
    }
    .section-title {
        color: var(--primary-green);
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .event-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .event-item {
        margin-bottom: 0.75rem;
        color: var(--text-main);
    }
    .event-date {
        color: var(--primary-green);
        font-weight: 600;
        margin-left: 0.5rem;
    }
</style>

<div class="banner">Blessed Sacrament Church</div>

<div class="card">
    <div class="section-title">Next Service</div>
    <div><b>Date:</b> {nextService.date}</div>
    <div><b>Time:</b> {nextService.time}</div>
    <div><b>Address:</b> {nextService.address}</div>
</div>

<div class="card">
    <div class="section-title">Upcoming Events</div>
    <ul class="event-list">
        {#each events as e}
            <li class="event-item">{e.name} <span class="event-date">({e.date}, {e.time})</span></li>
        {/each}
    </ul>
</div> 