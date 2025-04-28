<script>
    let communities = [
        {
            name: 'Rides to School',
            slug: 'rides',
            bannerColor: 'linear-gradient(90deg, var(--primary-green), var(--primary-brown))',
            description: 'Find and offer rides for high school students. View and sign up for available slots!',
            calendarPreview: [
                { date: 'Mon', slots: 2 },
                { date: 'Tue', slots: 1 },
                { date: 'Wed', slots: 3 }
            ]
        },
        {
            name: 'Little League Baseball',
            slug: 'baseball',
            bannerColor: 'linear-gradient(90deg, var(--primary-brown), var(--primary-green))',
            description: 'Join the fun! See team photos and upcoming games or practices.',
            images: ['/field.jpg', '/team.jpg'],
            nextEvent: 'Practice: Sat 10am'
        },
        {
            name: 'Book Club',
            slug: 'book-club',
            bannerColor: 'linear-gradient(90deg, var(--primary-green), var(--primary-brown))',
            description: 'Monthly reads and lively discussions. Next: "The Great Gatsby". Next event: Friday, May 17, 7:00pm at 123 Maple Ave.'
        },
        {
            name: 'Blessed Sacrament Church',
            slug: 'blessed-sacrament-church',
            bannerColor: 'linear-gradient(90deg, var(--primary-brown), var(--primary-green))',
            description: 'Next service: Sunday, May 12, 10:30am. 456 Church St. Upcoming: Youth Group, Choir, Potluck.'
        },
        {
            name: 'Friends of Washington Grove',
            slug: 'friends-of-washington-grove',
            bannerColor: 'linear-gradient(90deg, var(--primary-green), var(--primary-brown))',
            description: 'Help keep the park clean! Next: Spring Cleanup, Sat, May 18, 9:00am. "Looking forward to the next cleanup!"'
        }
    ];

    let search = '';
    let invites = [
        { name: 'Chess Club', from: 'Alex' },
        { name: 'Makerspace', from: 'Jordan' }
    ];
    let suggestions = [
        { name: 'Running Club' },
        { name: 'Photography' }
    ];
</script>

<style>
    :root {
        --primary-green: #2d5a27;
        --primary-brown: #8b4513;
        --accent-gold: #d4af37;
        --background: #f5f5f0;
        --card-bg: #fff;
        --card-shadow: 0 4px 12px rgba(43, 43, 43, 0.1);
        --border-radius: 12px;
        --text-main: #2d2d2d;
        --text-muted: #666;
    }

    .top-section {
        max-width: 1200px;
        margin: 2rem auto 1.5rem auto;
        display: flex;
        flex-wrap: wrap;
        gap: 2rem;
        align-items: flex-start;
    }
    .search-box {
        flex: 2;
        min-width: 300px;
    }
    .search-input {
        width: 100%;
        padding: 0.75rem 1rem;
        border-radius: var(--border-radius);
        border: 1px solid rgba(139, 69, 19, 0.2);
        font-size: 1.1rem;
        background: #fff;
        transition: border-color 0.3s;
    }
    .search-input:focus {
        outline: none;
        border-color: var(--primary-green);
    }
    .suggested, .invites {
        flex: 1;
        min-width: 220px;
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        padding: 1rem 1.25rem;
        border: 1px solid rgba(139, 69, 19, 0.1);
    }
    .section-title {
        color: var(--primary-green);
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .invite-item, .suggest-item {
        margin-bottom: 0.5rem;
        color: var(--text-main);
    }
    .invite-from {
        color: var(--primary-brown);
        font-size: 0.95rem;
    }
    .communities-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 2rem;
        max-width: 1200px;
        margin: 0 auto 2rem auto;
    }
    .community-card {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        overflow: hidden;
        display: flex;
        flex-direction: column;
        min-height: 320px;
        border: 1px solid rgba(139, 69, 19, 0.1);
    }
    .community-banner {
        padding: 1.2rem 1.5rem;
        color: #fff;
        font-size: 1.5rem;
        font-weight: 700;
        text-shadow: 0 2px 8px rgba(44, 62, 80, 0.12);
        background: var(--primary-green);
    }
    .community-content {
        flex: 1;
        padding: 1.2rem 1.5rem;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .calendar-preview {
        display: flex;
        gap: 1rem;
        margin: 0.5rem 0 1rem 0;
    }
    .calendar-day {
        background: var(--primary-brown);
        color: #fff;
        border-radius: 8px;
        padding: 0.5rem 0.75rem;
        text-align: center;
        font-size: 1rem;
        min-width: 48px;
    }
    .photo-preview {
        display: flex;
        gap: 0.5rem;
        margin: 0.5rem 0 1rem 0;
    }
    .photo-preview img {
        width: 60px;
        height: 60px;
        object-fit: cover;
        border-radius: 8px;
        border: 2px solid var(--primary-green);
    }
    .view-btn {
        background: var(--primary-green);
        color: #fff;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        margin-top: 1rem;
        align-self: flex-end;
        transition: all 0.3s;
    }
    .view-btn:hover {
        background: var(--primary-brown);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(43, 43, 43, 0.2);
    }
</style>

<div class="top-section">
    <div class="search-box">
        <input class="search-input" type="text" placeholder="Search for new groups..." bind:value={search} />
    </div>
    <div class="suggested">
        <div class="section-title">Suggested Groups</div>
        {#each suggestions as s}
            <div class="suggest-item">+ {s.name}</div>
        {/each}
    </div>
    <div class="invites">
        <div class="section-title">Invites</div>
        {#if invites.length === 0}
            <div class="invite-item">No invites</div>
        {:else}
            {#each invites as i}
                <div class="invite-item">{i.name} <span class="invite-from">from {i.from}</span></div>
            {/each}
        {/if}
    </div>
</div>

<div class="communities-grid">
    {#each communities as c}
        <div class="community-card">
            <div class="community-banner">{c.name}</div>
            <div class="community-content">
                <div>{c.description}</div>
                {#if c.calendarPreview}
                    <div class="calendar-preview">
                        {#each c.calendarPreview as day}
                            <div class="calendar-day">{day.date}<br /><span style="font-size:0.9em">{day.slots} slots</span></div>
                        {/each}
                    </div>
                {/if}
                {#if c.images}
                    <div class="photo-preview">
                        {#each c.images as img}
                            <img src={img} alt="Community photo" />
                        {/each}
                    </div>
                    <div style="color: var(--primary-green); font-weight: 600;">{c.nextEvent}</div>
                {/if}
                <a href={`/community/${c.slug}`}><button class="view-btn">View</button></a>
            </div>
        </div>
    {/each}
</div>