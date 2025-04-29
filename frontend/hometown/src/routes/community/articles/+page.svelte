<script>
    let articles = [
        {
            id: 1,
            title: 'Community Garden Project Takes Root',
            author: 'Sarah Johnson',
            date: 'May 1, 2024',
            excerpt: 'The new community garden initiative has officially launched, bringing together neighbors to grow fresh produce and build connections.',
            content: `The community garden project, which began as a small idea during last year's neighborhood meeting, has now blossomed into a thriving initiative. Located at the corner of Maple and Oak streets, the garden features 20 raised beds, a composting area, and a small greenhouse.

            "We've seen incredible enthusiasm from the community," says project coordinator Sarah Johnson. "Over 50 families have signed up to maintain plots, and we've already harvested our first batch of vegetables."

            The garden not only provides fresh produce but also serves as an educational space for local schools and a gathering place for neighbors. Weekly workshops on sustainable gardening practices are held every Saturday morning.

            Future plans include expanding the garden to include a children's learning area and installing a rainwater collection system. The project has received support from local businesses and the city council, with plans to replicate the model in other neighborhoods.`
        },
        {
            id: 2,
            title: 'Annual Spring Festival Draws Record Crowd',
            author: 'Michael Chen',
            date: 'April 28, 2024',
            excerpt: 'This year\'s Spring Festival broke attendance records with over 5,000 visitors enjoying local food, music, and crafts.',
            content: `The 15th Annual Spring Festival was a resounding success, drawing visitors from across the region to celebrate the season. Held in Washington Grove Park, the event featured over 100 local vendors, three stages of live music, and activities for all ages.

            "The energy this year was incredible," said festival organizer Michael Chen. "We saw a 30% increase in attendance compared to last year, and the feedback has been overwhelmingly positive."

            Highlights included:
            - A farmers' market showcasing local produce
            - Live performances from 20 local bands
            - Children's activities including face painting and crafts
            - Food trucks offering diverse cuisines
            - Artisan market with handmade goods

            The festival also raised over $10,000 for local schools through ticket sales and donations. Plans are already underway for next year's event, with organizers promising even more attractions and activities.`
        }
    ];

    let selectedArticle = null;
</script>

<style>
    .articles-container {
        max-width: 900px;
        margin: 2rem auto;
        padding: 0 1rem;
    }

    .article-card {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        padding: 2rem;
        margin-bottom: 2rem;
        cursor: pointer;
        transition: all 0.3s;
    }

    .article-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(43, 43, 43, 0.15);
    }

    .article-title {
        color: var(--primary-green);
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .article-meta {
        color: var(--text-muted);
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }

    .article-excerpt {
        color: var(--text-main);
        line-height: 1.6;
    }

    .article-content {
        color: var(--text-main);
        line-height: 1.8;
        margin-top: 2rem;
        white-space: pre-line;
    }

    .back-btn {
        background: var(--primary-green);
        color: #fff;
        border: none;
        border-radius: var(--border-radius);
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        margin-bottom: 2rem;
        transition: all 0.3s;
    }

    .back-btn:hover {
        background: var(--primary-brown);
        transform: translateY(-2px);
    }
</style>

<div class="articles-container">
    {#if selectedArticle}
        <button class="back-btn" on:click={() => selectedArticle = null}>← Back to Articles</button>
        <div class="article-card">
            <h1 class="article-title">{selectedArticle.title}</h1>
            <div class="article-meta">By {selectedArticle.author} | {selectedArticle.date}</div>
            <div class="article-content">{selectedArticle.content}</div>
        </div>
    {:else}
        {#each articles as article}
            <div class="article-card" on:click={() => selectedArticle = article}>
                <h2 class="article-title">{article.title}</h2>
                <div class="article-meta">By {article.author} | {article.date}</div>
                <div class="article-excerpt">{article.excerpt}</div>
            </div>
        {/each}
    {/if}
</div> 