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
    .banner {
        background: linear-gradient(90deg, #2d2dff, #7c3aed);
        color: #fff;
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin: 2rem auto 1.5rem auto;
        max-width: 900px;
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
    }
    .gallery {
        display: flex;
        gap: 1.5rem;
        justify-content: center;
        margin: 0 auto 2rem auto;
        max-width: 900px;
        background: #fff;
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
        padding: 2rem 1rem;
    }
    .gallery img {
        width: 220px;
        height: 160px;
        object-fit: cover;
        border-radius: 12px;
        border: 2px solid #2d2dff;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.10);
    }
    .calendar {
        background: #fff;
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
        padding: 2rem;
        margin: 0 auto 2rem auto;
        max-width: 900px;
    }
    .calendar-table {
        width: 100%;
        border-collapse: collapse;
    }
    .calendar-table th, .calendar-table td {
        padding: 1rem;
        border-bottom: 1px solid #ececec;
        text-align: left;
    }
    .calendar-table th {
        color: #2d2dff;
        font-size: 1.1rem;
    }
    .calendar-table td {
        color: #7c3aed;
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
    <h2 style="color:#2d2dff; margin-bottom:1rem;">Upcoming Games & Practices</h2>
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