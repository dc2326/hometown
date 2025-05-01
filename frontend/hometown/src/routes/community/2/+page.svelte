<script>
    let images = ['/field.jpg', '/team.jpg'];
    let events = [
        { date: 'Sat, May 11', type: 'Practice', time: '10:00am', location: 'Main Field' },
        { date: 'Mon, May 13', type: 'Game', time: '5:30pm', location: 'Field 2' },
        { date: 'Wed, May 15', type: 'Practice', time: '4:00pm', location: 'Main Field' },
        { date: 'Fri, May 17', type: 'Game', time: '6:00pm', location: 'Field 1' }
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
        max-width: 900px;
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        box-shadow: 0 2px 8px rgba(45, 90, 39, 0.15);
    }

    .gallery {
        display: flex;
        gap: 1.5rem;
        justify-content: center;
        margin: 0 auto 2rem auto;
        max-width: 900px;
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        padding: 2rem 1rem;
        border: 1px solid rgba(45, 90, 39, 0.1);
    }

    .gallery img {
        width: 220px;
        height: 160px;
        object-fit: cover;
        border-radius: var(--border-radius);
        border: 2px solid var(--primary-green);
        box-shadow: 0 2px 8px rgba(45, 90, 39, 0.15);
    }

    .calendar {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        padding: 2rem;
        margin: 0 auto 2rem auto;
        max-width: 900px;
        border: 1px solid rgba(45, 90, 39, 0.1);
    }

    .calendar-table {
        width: 100%;
        border-collapse: collapse;
    }

    .calendar-table th, .calendar-table td {
        padding: 1rem;
        border-bottom: 1px solid rgba(45, 90, 39, 0.1);
        text-align: left;
    }

    .calendar-table th {
        color: var(--primary-green);
        font-size: 1.1rem;
        font-weight: 600;
    }

    .calendar-table td {
        color: var(--text-main);
        font-size: 1rem;
    }
</style>

<div class="banner">Little League Baseball</div>

<div class="gallery">
    {#each images as img}
        <img src={img} alt="Little League photo" />
    {/each}
</div>

<div class="calendar">
    <h2 style="color:var(--primary-green); margin-bottom:1rem;">Upcoming Games & Practices</h2>
    <table class="calendar-table">
        <thead>
            <tr>
                <th>Date</th>
                <th>Type</th>
                <th>Time</th>
                <th>Location</th>
            </tr>
        </thead>
        <tbody>
            {#each events as e}
                <tr>
                    <td>{e.date}</td>
                    <td>{e.type}</td>
                    <td>{e.time}</td>
                    <td>{e.location}</td>
                </tr>
            {/each}
        </tbody>
    </table>
</div> 