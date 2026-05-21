document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const boardForm = document.getElementById('boardForm');
    const titleInput = document.getElementById('title');
    const messageInput = document.getElementById('message');
    const cardsGrid = document.getElementById('cardsGrid');
    const postCountBadge = document.getElementById('postCount');
    const toast = document.getElementById('toastNotification');

    // 1. Toast UX Feedback Toast Function
    const showToast = (message, type = 'success') => {
        toast.className = `toast show ${type}`;
        toast.innerHTML = `
            <i class="fa-solid ${type === 'success' ? 'fa-circle-check' : 'fa-circle-exclamation'}"></i>
            <span>${message}</span>
        `;
        
        // Hide Toast after 3.5s
        setTimeout(() => {
            toast.className = 'toast hidden';
        }, 3500);
    };

    // 2. Format database date
    const formatTime = (timeStr) => {
        if (!timeStr) return '';
        return timeStr.replace(/-/g, '/');
    };

    // 3. Create Card UI Component
    const createCardElement = (post, isNew = false) => {
        const card = document.createElement('article');
        card.className = `glass-card card-item ${isNew ? 'card-enter' : ''}`;
        card.id = `post-${post.id}`;

        card.innerHTML = `
            <button class="delete-btn" aria-label="생각 삭제" data-id="${post.id}">
                <i class="fa-solid fa-trash-can"></i>
            </button>
            <div class="card-body">
                <h3 class="card-title">${escapeHTML(post.title)}</h3>
                <p class="card-message">${escapeHTML(post.message)}</p>
            </div>
            <div class="card-footer">
                <span class="post-time">
                    <i class="fa-regular fa-clock"></i>
                    ${formatTime(post.created_at)}
                </span>
                <span class="card-vibe-tag">#aurora</span>
            </div>
        `;

        // Bind delete action
        const deleteBtn = card.querySelector('.delete-btn');
        deleteBtn.addEventListener('click', () => deletePost(post.id));

        return card;
    };

    // Prevent XSS Injection
    const escapeHTML = (str) => {
        return str
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    };

    // 4. Update count badge
    const updatePostCount = (count) => {
        postCountBadge.textContent = count;
    };

    // 5. Fetch posts
    const fetchPosts = async () => {
        try {
            const response = await fetch('/api/posts');
            if (!response.ok) throw new Error('이야기들을 가져오는 데 실패했습니다.');
            
            const posts = await response.json();
            cardsGrid.innerHTML = '';
            
            if (posts.length === 0) {
                cardsGrid.innerHTML = `
                    <div class="no-posts-container">
                        <i class="fa-solid fa-meteor"></i>
                        <p>아직 피드가 고요합니다. 첫 번째 빛나는 영감을 띄워보세요.</p>
                    </div>
                `;
                updatePostCount(0);
                return;
            }

            posts.forEach(post => {
                const card = createCardElement(post);
                cardsGrid.appendChild(card);
            });
            
            updatePostCount(posts.length);
        } catch (error) {
            console.error(error);
            cardsGrid.innerHTML = '';
            showToast(error.message, 'error');
        }
    };

    // 6. Submit Post
    boardForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const title = titleInput.value.trim();
        const message = messageInput.value.trim();

        if (!title) {
            showToast('영감의 제목을 채워주세요.', 'error');
            titleInput.focus();
            return;
        }
        if (!message) {
            showToast('이야기를 채워주세요.', 'error');
            messageInput.focus();
            return;
        }

        try {
            const submitBtn = document.getElementById('btn-submit-vibe');
            submitBtn.disabled = true;
            submitBtn.style.opacity = '0.6';

            const response = await fetch('/api/posts', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title, message })
            });

            if (!response.ok) {
                const errData = await response.json();
                throw new Error(errData.error || '이야기를 우주 피드에 띄우지 못했습니다.');
            }

            const newPost = await response.json();
            
            // Clear 'No posts' text
            const noPosts = cardsGrid.querySelector('.no-posts-container');
            if (noPosts) {
                cardsGrid.innerHTML = '';
            }

            // Create card and insert with spring-bounce animation
            const newCard = createCardElement(newPost, true);
            cardsGrid.insertBefore(newCard, cardsGrid.firstChild);

            // Re-calculate
            const currentCount = parseInt(postCountBadge.textContent) || 0;
            updatePostCount(currentCount + 1);

            boardForm.reset();
            showToast('당신의 아름다운 영감이 오로라 피드에 안착했습니다! 🌌');
            
            submitBtn.disabled = false;
            submitBtn.style.opacity = '1';
            
        } catch (error) {
            console.error(error);
            showToast(error.message, 'error');
            
            const submitBtn = document.getElementById('btn-submit-vibe');
            submitBtn.disabled = false;
            submitBtn.style.opacity = '1';
        }
    });

    // 7. Delete Post
    const deletePost = async (id) => {
        if (!confirm('이 영감 조각을 우주 피드에서 영구히 삭제하시겠습니까?')) return;

        try {
            const response = await fetch(`/api/posts/${id}`, {
                method: 'DELETE'
            });

            if (!response.ok) {
                const errData = await response.json();
                throw new Error(errData.error || '삭제하지 못했습니다.');
            }

            const targetCard = document.getElementById(`post-${id}`);
            if (targetCard) {
                // Trigger exit shrink scaling animation
                targetCard.classList.add('card-exit');
                
                setTimeout(() => {
                    targetCard.remove();
                    
                    const currentCount = parseInt(postCountBadge.textContent) || 0;
                    const newCount = Math.max(0, currentCount - 1);
                    updatePostCount(newCount);

                    if (newCount === 0) {
                        cardsGrid.innerHTML = `
                            <div class="no-posts-container">
                                <i class="fa-solid fa-meteor"></i>
                                <p>아직 피드가 고요합니다. 첫 번째 빛나는 영감을 띄워보세요.</p>
                            </div>
                        `;
                    }
                }, 400); // 0.4s duration matching scale-out
            }

            showToast('영감이 은하수 뒤편으로 사라졌습니다.');
        } catch (error) {
            console.error(error);
            showToast(error.message, 'error');
        }
    };

    // Initialize Page
    fetchPosts();
});
