<script>
    let communityTypes = [
        'Rideshare',
        'Sports',
        'Non-Profit',
        'Book Club',
        'Religious',
        'Community Service',
        'Other'
    ];

    let functionalityOptions = [
        { id: 'calendar', label: 'Calendar/Events', description: 'Schedule and manage events' },
        { id: 'messaging', label: 'Messaging', description: 'Group chat and announcements' },
        { id: 'photoGallery', label: 'Photo Gallery', description: 'Share and view photos' },
        { id: 'memberDirectory', label: 'Member Directory', description: 'List of community members' },
        { id: 'signupSheet', label: 'Signup Sheet', description: 'Volunteer and event signups' }
    ];

    let formData = {
        name: '',
        type: '',
        description: '',
        selectedFunctionality: []
    };

    function handleSubmit() {
        // Here we would typically send the data to a backend
        console.log('Form submitted:', formData);
        // For now, we'll just show an alert
        alert('Community created successfully!');
    }
</script>

<style>
    .create-form {
        max-width: 800px;
        margin: 2rem auto;
        padding: 2rem;
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
    }

    .form-title {
        color: var(--primary-green);
        font-size: 2rem;
        margin-bottom: 2rem;
        text-align: center;
    }

    .form-group {
        margin-bottom: 1.5rem;
    }

    .form-label {
        display: block;
        color: var(--text-main);
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .form-input, .form-select, .form-textarea {
        width: 100%;
        padding: 0.75rem;
        border: 1px solid rgba(139, 69, 19, 0.2);
        border-radius: var(--border-radius);
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }

    .form-input:focus, .form-select:focus, .form-textarea:focus {
        outline: none;
        border-color: var(--primary-green);
    }

    .functionality-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }

    .functionality-option {
        border: 1px solid rgba(139, 69, 19, 0.2);
        border-radius: var(--border-radius);
        padding: 1rem;
        cursor: pointer;
        transition: all 0.3s;
    }

    .functionality-option:hover {
        border-color: var(--primary-green);
        background: rgba(45, 90, 39, 0.05);
    }

    .functionality-option.selected {
        border-color: var(--primary-green);
        background: rgba(45, 90, 39, 0.1);
    }

    .functionality-label {
        font-weight: 600;
        color: var(--text-main);
        margin-bottom: 0.5rem;
    }

    .functionality-description {
        font-size: 0.9rem;
        color: var(--text-muted);
    }

    .submit-btn {
        background: var(--primary-green);
        color: #fff;
        border: none;
        border-radius: var(--border-radius);
        padding: 1rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        width: 100%;
        margin-top: 2rem;
        transition: all 0.3s;
    }

    .submit-btn:hover {
        background: var(--primary-brown);
        transform: translateY(-2px);
    }
</style>

<div class="create-form">
    <h1 class="form-title">Create a New Community</h1>
    
    <form on:submit|preventDefault={handleSubmit}>
        <div class="form-group">
            <label class="form-label" for="name">Community Name</label>
            <input
                class="form-input"
                type="text"
                id="name"
                bind:value={formData.name}
                required
                placeholder="Enter community name"
            />
        </div>

        <div class="form-group">
            <label class="form-label" for="type">Community Type</label>
            <select class="form-select" id="type" bind:value={formData.type} required>
                <option value="">Select a type</option>
                {#each communityTypes as type}
                    <option value={type}>{type}</option>
                {/each}
            </select>
        </div>

        <div class="form-group">
            <label class="form-label" for="description">Description</label>
            <textarea
                class="form-textarea"
                id="description"
                bind:value={formData.description}
                rows="4"
                required
                placeholder="Describe your community..."
            ></textarea>
        </div>

        <div class="form-group">
            <label class="form-label">Select Functionality</label>
            <div class="functionality-grid">
                {#each functionalityOptions as option}
                    <div
                        class="functionality-option"
                        class:selected={formData.selectedFunctionality.includes(option.id)}
                        on:click={() => {
                            if (formData.selectedFunctionality.includes(option.id)) {
                                formData.selectedFunctionality = formData.selectedFunctionality.filter(id => id !== option.id);
                            } else {
                                formData.selectedFunctionality = [...formData.selectedFunctionality, option.id];
                            }
                        }}
                    >
                        <div class="functionality-label">{option.label}</div>
                        <div class="functionality-description">{option.description}</div>
                    </div>
                {/each}
            </div>
        </div>

        <button type="submit" class="submit-btn">Create Community</button>
    </form>
</div> 