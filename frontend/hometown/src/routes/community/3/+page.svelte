<script>
    let nextEvent = {
        date: 'Friday, May 17',
        time: '7:00pm',
        host: 'Emily R.',
        address: '123 Maple Ave, Community Room B'
    };
    let upcomingBooks = [
        'The Great Gatsby',
        'To Kill a Mockingbird',
        '1984'
    ];
    let voteOptions = [
        { title: 'Pride and Prejudice', votes: 3 },
        { title: 'The Hobbit', votes: 5 },
        { title: 'The Catcher in the Rye', votes: 2 }
    ];
    function vote(idx) {
        voteOptions[idx].votes++;
    }
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
    .vote-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .vote-item {
        display: flex;
        align-items: center;
        margin-bottom: 0.75rem;
    }
    .vote-btn {
        background: linear-gradient(90deg, #7c3aed, #2d2dff);
        color: #fff;
        border: none;
        border-radius: 8px;
        padding: 0.4rem 1rem;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        margin-right: 1rem;
        transition: background 0.2s;
    }
    .vote-btn:hover {
        background: linear-gradient(90deg, #2d2dff, #7c3aed);
    }
    .votes {
        color: #7c3aed;
        font-weight: 600;
        margin-left: 0.5rem;
    }
</style>

<div class="banner">Book Club</div>

<div class="card">
    <div class="section-title">Next Event</div>
    <div><b>Date:</b> {nextEvent.date}</div>
    <div><b>Time:</b> {nextEvent.time}</div>
    <div><b>Host:</b> {nextEvent.host}</div>
    <div><b>Address:</b> {nextEvent.address}</div>
</div>

<div class="card">
    <div class="section-title">Upcoming Books</div>
    <ul>
        {#each upcomingBooks as book}
            <li>{book}</li>
        {/each}
    </ul>
</div>

<div class="card">
    <div class="section-title">Vote for the Next Book</div>
    <ul class="vote-list">
        {#each voteOptions as option, idx}
            <li class="vote-item">
                <button class="vote-btn" on:click={() => vote(idx)}>Vote</button>
                {option.title} <span class="votes">({option.votes} votes)</span>
            </li>
        {/each}
    </ul>
</div> 