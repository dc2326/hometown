<script>
    let article = {
        title: 'Park Volunteer Day Announced',
        date: 'May 8, 2024',
        author: 'Lisa Thompson',
        readTime: '2 min read',
        content: `
            The Friends of Washington Grove organization has announced their next community volunteer day, scheduled for this Saturday from 9:00 AM to 2:00 PM. This event marks the beginning of the park's revitalization project and offers community members a chance to get involved in shaping their local green space.

            Volunteers will have the opportunity to participate in various activities:
            • Planting new trees and shrubs
            • Installing raised garden beds
            • Cleaning up walking trails
            • Assembling new park benches

            "We're expecting a great turnout," says event coordinator Mark Reynolds. "These volunteer days are always popular because they give people a chance to make a real difference in their community while meeting their neighbors."

            All necessary tools and equipment will be provided, and volunteers are encouraged to bring their own work gloves and water bottles. Lunch will be provided for all participants.

            The event is open to all ages, though children under 12 must be accompanied by an adult. No prior experience is necessary, and training will be provided for all tasks.

            To sign up or get more information, visit the Friends of Washington Grove website or call the community center at (555) 123-4567.
        `
    };
</script>

<style>
    :root {
        --primary-green: #2d5a27;
        --light-green: #3a7a33;
        --background: #f5f5f0;
        --card-bg: #fff;
        --border-radius: 12px;
        --text-main: #222;
        --text-muted: #666;
    }

    .article-container {
        max-width: 800px;
        margin: 2rem auto;
        padding: 0 1rem;
    }

    .article-header {
        margin-bottom: 2rem;
    }

    .article-title {
        font-size: 2.5rem;
        color: var(--primary-green);
        margin-bottom: 1rem;
        line-height: 1.2;
    }

    .article-meta {
        color: var(--light-green);
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .article-content {
        font-size: 1.1rem;
        line-height: 1.6;
        color: var(--text-main);
    }

    .article-content p {
        margin-bottom: 1.5rem;
    }
</style>

<div class="article-container">
    <div class="article-header">
        <h1 class="article-title">{article.title}</h1>
        <div class="article-meta">
            By {article.author} • {article.date} • {article.readTime}
        </div>
    </div>
    <div class="article-content">
        {#each article.content.split('\n') as paragraph}
            {#if paragraph.trim()}
                <p>{paragraph}</p>
            {/if}
        {/each}
    </div>
</div> 