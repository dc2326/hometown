<script>
    let article = {
        title: 'Park Receives Green Space Grant',
        date: 'May 4, 2024',
        author: 'Sarah Johnson',
        readTime: '2 min read',
        content: `
            The Washington Grove Park has been awarded a $500,000 Green Space Enhancement Grant from the State Department of Environmental Conservation. This funding will support the installation of new trees, benches, and accessibility features throughout the park.

            "This grant is a game-changer for our community," says Parks Director Maria Gonzalez. "It will allow us to make significant improvements to the park's infrastructure while maintaining its natural beauty."

            The grant will fund:
            • 50 new native trees
            • 20 new park benches with accessibility features
            • Improved trail surfaces for wheelchair access
            • New interpretive signs about local flora and fauna
            • Solar-powered lighting along main pathways

            The improvements are part of a larger effort to make the park more accessible and environmentally sustainable. The new trees will help reduce the urban heat island effect, while the solar lighting will cut energy costs by 40%.

            "We're particularly excited about the accessibility improvements," says community advocate Tom Wilson. "These changes will ensure that everyone in our community can enjoy the park, regardless of their mobility needs."

            Work on the improvements is expected to begin in early June and will be completed in phases over the next six months. The park will remain open during construction, with temporary detours in place as needed.

            The grant was secured through a joint effort by the Parks Department and the Friends of Washington Grove organization. Community members can track the progress of the improvements through the town's website and monthly progress reports.

            For more information about the grant and upcoming park improvements, visit www.washingtongrove.org/greenspace or attend the next Parks Advisory Committee meeting on May 20th.
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