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
    .banner {
        background: linear-gradient(90deg, #7c3aed, #2d2dff);
        color: #fff;
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin: 2rem auto 1.5rem auto;
        max-width: 700px;
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
    }
    .card {
        background: #fff;
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
        padding: 2rem;
        margin: 0 auto 2rem auto;
        max-width: 700px;
    }
    .section-title {
        color: #2d2dff;
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
        color: #22223b;
    }
    .event-date {
        color: #7c3aed;
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