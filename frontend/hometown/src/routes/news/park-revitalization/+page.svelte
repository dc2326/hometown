<script>
    let article = {
        title: 'Park Revitalization Project Underway',
        date: 'May 15, 2024',
        author: 'Sarah Johnson',
        readTime: '5 min read',
        image: '/park.jpg',
        content: `
            The town has officially begun its ambitious park revitalization project, which aims to transform our central green space into a modern, accessible, and environmentally friendly community hub. The project, which has been in planning for over a year, finally broke ground last week.

            Phase one of the project includes:
            • New walking trails with accessibility features
            • A state-of-the-art playground with inclusive equipment
            • Community gardens with raised beds
            • Improved lighting and security features

            "This is more than just a park upgrade," says Mayor Thompson. "It's about creating a space that brings our community together and serves everyone's needs."

            The project is expected to be completed in phases over the next 18 months, with the first section opening to the public by late summer. Community members are encouraged to participate in volunteer days throughout the construction period.

            Funding for the $2.5 million project comes from a combination of city funds, state grants, and private donations. The Friends of Washington Grove organization has been instrumental in raising awareness and securing additional funding.

            Residents can stay updated on the project's progress through the town's website and monthly community meetings. The next public meeting is scheduled for June 5th at the community center.
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

    .article-image {
        width: 100%;
        height: 400px;
        object-fit: cover;
        border-radius: var(--border-radius);
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
        <img class="article-image" src={article.image} alt={article.title} />
    </div>
    <div class="article-content">
        {#each article.content.split('\n') as paragraph}
            {#if paragraph.trim()}
                <p>{paragraph}</p>
            {/if}
        {/each}
    </div>
</div> 