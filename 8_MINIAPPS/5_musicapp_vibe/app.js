/**
 * VIBE: Premium Music SNS & Search Platform - Core Application Logic
 * Powered by Luxury Botanical Dark styling, LocalStorage DB, and YouTube oEmbed API.
 */

// ==========================================
// 1. MOCK DATABASE (VibeDB) & INITIALIZATION
// ==========================================

const VIBE_DB_KEYS = {
  USERS: 'vibe_users',
  MUSIC: 'vibe_music',
  COMMENTS: 'vibe_comments',
  NOTIFICATIONS: 'vibe_notifications',
  SESSION: 'vibe_session'
};

// Selection of high-quality premium avatars (Unsplash vectors)
const DEFAULT_AVATARS = [
  'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80',
  'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=100&auto=format&fit=crop&q=80',
  'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&auto=format&fit=crop&q=80',
  'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&auto=format&fit=crop&q=80',
  'https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=100&auto=format&fit=crop&q=80'
];

const VibeDB = {
  get(key) {
    try {
      const data = localStorage.getItem(key);
      return data ? JSON.parse(data) : null;
    } catch (e) {
      console.error("Error reading from LocalStorage:", e);
      return null;
    }
  },

  set(key, val) {
    try {
      localStorage.setItem(key, JSON.stringify(val));
    } catch (e) {
      console.error("Error writing to LocalStorage:", e);
    }
  },

  initialize() {
    // 1. Default Users Setup
    if (!this.get(VIBE_DB_KEYS.USERS)) {
      const defaultUsers = [
        { username: 'admin', password: 'admin123', role: 'admin', avatar: DEFAULT_AVATARS[0], joinedAt: '2026-01-10' },
        { username: 'vibe_maker', password: 'vibe123', role: 'user', avatar: DEFAULT_AVATARS[1], joinedAt: '2026-03-15' },
        { username: 'chill_listener', password: 'chill123', role: 'user', avatar: DEFAULT_AVATARS[2], joinedAt: '2026-04-01' }
      ];
      this.set(VIBE_DB_KEYS.USERS, defaultUsers);
    }

    // 2. Default Music Setup (14 Premium playable YouTube tracks with real IDs)
    const defaultMusic = [
      {
        id: 'm1',
        youtubeId: 'pSUydWEqKwE',
        title: 'NewJeans (뉴진스) - "Ditto"',
        desc: '뉴진스의 아련하고 몽환적인 윈터 감성곡. 독특한 볼티모어 클럽 댄스 비트와 감성적인 멜로디가 어우러져 추억을 자극합니다.',
        tags: ['겨울감성', '뉴진스', '인디팝', '몽환적인'],
        likes: ['vibe_maker', 'chill_listener'],
        createdBy: 'admin',
        createdAt: '2026-05-01T10:00:00Z'
      },
      {
        id: 'm2',
        youtubeId: '5qap5aO4i9A',
        title: 'Lofi Girl - "Lofi Hip Hop Radio" (Relaxing Beats)',
        desc: '공부할 때, 일할 때, 혹은 조용히 사색에 잠기고 싶을 때 듣기 좋은 글로벌 No.1 로파이 힙합 라디오 셀렉션.',
        tags: ['로파이', '공부할때', '잔잔한', '새벽'],
        likes: ['chill_listener'],
        createdBy: 'admin',
        createdAt: '2026-05-02T12:00:00Z'
      },
      {
        id: 'm3',
        youtubeId: 'hLvWy2b857I',
        title: 'LE SSERAFIM (르세라핌) - "Perfect Night"',
        desc: '오버화치2 콜라보레이션 음원. 동료들과 함께라면 완벽하지 않은 하루도 즐거울 수 있다는 긍정적인 메시지를 담은 이지리스닝 곡.',
        tags: ['드라이브', '이지리스닝', '르세라핌', '기분전환'],
        likes: ['vibe_maker'],
        createdBy: 'vibe_maker',
        createdAt: '2026-05-03T15:30:00Z'
      },
      {
        id: 'm4',
        youtubeId: 'gdZLi9oWNZg',
        title: 'BTS (방탄소년단) - "Dynamite"',
        desc: '전 세계를 디스코 열풍으로 빠뜨린 방탄소년단의 글로벌 메가 히트 송. 밝고 신나는 펑크 디스코 비트가 몸을 들썩이게 만듭니다.',
        tags: ['디스코', '신나는', '방탄소년단', '팝송'],
        likes: [],
        createdBy: 'admin',
        createdAt: '2026-05-04T09:00:00Z'
      },
      {
        id: 'm5',
        youtubeId: 'nM0xDI5R50E',
        title: 'IU (아이유) - "BBIBBI" (삐삐)',
        desc: '아이유의 힙하고 여유로운 알앤비/소울 트랙. 선을 넘는 사람들에게 던지는 유쾌하고 귀여운 경고장.',
        tags: ['아이유', '알앤비', '위트', '트렌디한'],
        likes: ['chill_listener'],
        createdBy: 'chill_listener',
        createdAt: '2026-05-05T18:20:00Z'
      },
      {
        id: 'm6',
        youtubeId: 'dvgZkm1xWPE',
        title: 'Coldplay - "Viva La Vida"',
        desc: '웅장한 현악 오케스트레이션과 크리스 마틴의 호소력 짙은 보컬이 돋보이는 얼터너티브 락의 명작.',
        tags: ['명곡', '락', '웅장한', '밴드'],
        likes: ['vibe_maker', 'admin'],
        createdBy: 'admin',
        createdAt: '2026-05-06T11:00:00Z'
      },
      {
        id: 'm7',
        youtubeId: 'd1REzQ75COs',
        title: 'Sunset Rollercoaster (낙일비차) - "My Jinji"',
        desc: '대만 출신의 시티팝/신스팝 밴드 낙일비차의 대표곡. 몽환적이고 레트로한 밴드 사운드로 낭만 가득한 새벽 감성을 완성합니다.',
        tags: ['시티팝', '인디밴드', '새벽', '레트로'],
        likes: ['chill_listener'],
        createdBy: 'vibe_maker',
        createdAt: '2026-05-07T22:00:00Z'
      },
      {
        id: 'm8',
        youtubeId: '6ZUIwj3FgUY',
        title: 'IVE (아이브) - "I AM"',
        desc: '내가 가는 길에 확신을 가지라는 당당한 자기 주체성의 메시지. 폭발적인 보컬과 웅장한 신스 드럼이 매력적인 댄스 팝.',
        tags: ['아이브', '신나는', '보컬', '자존감'],
        likes: [],
        createdBy: 'chill_listener',
        createdAt: '2026-05-08T14:40:00Z'
      }
    ];

    if (!this.get(VIBE_DB_KEYS.MUSIC)) {
      this.set(VIBE_DB_KEYS.MUSIC, defaultMusic);
    } else {
      // 5. Automatic Video ID Rematching Fix (Forced Sync based on defaultMusic metadata)
      let dbMusic = this.get(VIBE_DB_KEYS.MUSIC);
      if (dbMusic) {
        let changed = false;
        dbMusic.forEach(track => {
          const matchingDefault = defaultMusic.find(dm => dm.id === track.id);
          if (matchingDefault && track.youtubeId !== matchingDefault.youtubeId) {
            track.youtubeId = matchingDefault.youtubeId;
            track.title = matchingDefault.title;
            track.desc = matchingDefault.desc;
            changed = true;
          }
        });
        if (changed) {
          this.set(VIBE_DB_KEYS.MUSIC, dbMusic);
        }
      }
    }

    // 3. Default Comments Setup
    if (!this.get(VIBE_DB_KEYS.COMMENTS)) {
      const defaultComments = [
        {
          id: 'c1',
          musicId: 'm1',
          username: 'chill_listener',
          avatar: DEFAULT_AVATARS[2],
          content: '진짜 전주 부분 흐를 때 온몸에 소름 돋아요.. 겨울에 듣는 디토는 예술입니다 ㅠㅠ',
          timestamp: '2026-05-18T14:32:00Z'
        },
        {
          id: 'c2',
          musicId: 'm1',
          username: 'vibe_maker',
          avatar: DEFAULT_AVATARS[1],
          content: '뮤직비디오 세계관이랑 같이 들으면 눈물샘 자극 대박이에요.',
          timestamp: '2026-05-19T09:15:00Z'
        },
        {
          id: 'c3',
          musicId: 'm3',
          username: 'chill_listener',
          avatar: DEFAULT_AVATARS[2],
          content: '드라이브할 때 가볍게 흥얼거리기 최고의 이지리스닝 곡!',
          timestamp: '2026-05-20T17:45:00Z'
        },
        {
          id: 'c4',
          musicId: 'm2',
          username: 'admin',
          avatar: DEFAULT_AVATARS[0],
          content: 'Vibe 커뮤니티 공간에 오신 것을 환영합니다. 서로 존중하는 댓글 문화를 만들어가요.',
          timestamp: '2026-05-21T02:00:00Z'
        }
      ];
      this.set(VIBE_DB_KEYS.COMMENTS, defaultComments);
    }

    // 4. Default Notifications Setup
    if (!this.get(VIBE_DB_KEYS.NOTIFICATIONS)) {
      this.set(VIBE_DB_KEYS.NOTIFICATIONS, []);
    }
  }
};

// Initialize Database on startup
VibeDB.initialize();

// ==========================================
// 2. GLOBAL STATE & ROUTING
// ==========================================

const AppState = {
  currentUser: VibeDB.get(VIBE_DB_KEYS.SESSION), // { username, role, avatar } or null
  activePage: 'feed',
  currentPlayingTrack: null, // music item object
  playlist: [], // active list of tracks
  searchType: 'all', // all, title, desc, tag
  adminActiveTab: 'members', // members, posts, comments
  activeMusicDetailId: null // ID of open music details modal
};

// Simple Client Side SPA Routing
function showPage(pageId) {
  AppState.activePage = pageId;
  
  // Toggle page view sections
  document.querySelectorAll('.page-view').forEach(view => {
    if (view.id === `page-${pageId}`) {
      view.classList.add('active');
    } else {
      view.classList.remove('active');
    }
  });

  // Specific view loaders
  if (pageId === 'feed') {
    renderFeedPage();
  } else if (pageId === 'search') {
    const q = document.getElementById('global-search-input').value.trim();
    renderSearchPage(q);
  } else if (pageId === 'profile') {
    renderProfilePage();
  } else if (pageId === 'admin') {
    renderAdminPage();
  }

  // Scroll to top
  document.querySelector('.app-main').scrollTop = 0;
}

// Global UI Notifications
function showToast(message, type = 'success') {
  const container = document.getElementById('toast-box');
  const toast = document.createElement('div');
  toast.className = 'toast';
  
  const iconSvg = `
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="10"></circle><polyline points="12 8 12 12 16 14"></polyline>
    </svg>
  `;
  
  toast.innerHTML = `${iconSvg} <span>${message}</span>`;
  container.appendChild(toast);
  
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translate(-50%, -10px)';
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

// ==========================================
// 3. AUTHENTICATION & SESSION MANAGEMENT
// ==========================================

function updateHeaderUserWidget() {
  const widget = document.getElementById('user-header-widget');
  const adminBtn = document.getElementById('btn-admin-console');

  if (AppState.currentUser) {
    widget.innerHTML = `
      <button class="user-avatar-trigger" id="header-profile-btn" title="마이페이지 이동">
        <img src="${AppState.currentUser.avatar || DEFAULT_AVATARS[0]}" alt="Avatar">
        <span>${AppState.currentUser.username}</span>
      </button>
    `;
    
    // Bind click to go to profile
    document.getElementById('header-profile-btn').addEventListener('click', () => {
      showPage('profile');
    });

    // Toggle Admin navigation visibility
    if (AppState.currentUser.role === 'admin') {
      if (adminBtn) adminBtn.classList.remove('hidden');
    } else {
      if (adminBtn) adminBtn.classList.add('hidden');
    }
  } else {
    widget.innerHTML = `<button class="btn-login" id="btn-trigger-auth">로그인</button>`;
    document.getElementById('btn-trigger-auth').addEventListener('click', openAuthDialog);
    if (adminBtn) adminBtn.classList.add('hidden');
  }
}

// Dialog Toggles
function openAuthDialog() {
  const dialog = document.getElementById('auth-dialog');
  dialog.style.display = 'flex';
  setTimeout(() => dialog.classList.add('active'), 10);
  renderAvatarSelectionGrid();
}

function closeAuthDialog() {
  const dialog = document.getElementById('auth-dialog');
  dialog.classList.remove('active');
  setTimeout(() => dialog.style.display = 'none', 300);
}

function renderAvatarSelectionGrid() {
  const grid = document.getElementById('signup-avatar-grid');
  grid.innerHTML = '';
  DEFAULT_AVATARS.forEach((src, idx) => {
    const opt = document.createElement('div');
    opt.className = `avatar-option ${idx === 0 ? 'selected' : ''}`;
    opt.dataset.src = src;
    opt.innerHTML = `<img src="${src}" alt="character ${idx}">`;
    opt.addEventListener('click', () => {
      document.querySelectorAll('.avatar-option').forEach(el => el.classList.remove('selected'));
      opt.classList.add('selected');
    });
    grid.appendChild(opt);
  });
}

// Handles user signup
function handleSignUpSubmit() {
  const userIn = document.getElementById('signup-username').value.trim();
  const passIn = document.getElementById('signup-password').value;
  const avatarEl = document.querySelector('.avatar-option.selected');
  const avatarUrl = avatarEl ? avatarEl.dataset.src : DEFAULT_AVATARS[0];

  if (userIn.length < 3) {
    alert('아이디는 최소 3자 이상이어야 합니다.');
    return;
  }
  if (passIn.length < 4) {
    alert('비밀번호는 최소 4자 이상 설정해야 합니다.');
    return;
  }

  const users = VibeDB.get(VIBE_DB_KEYS.USERS) || [];
  const exists = users.some(u => u.username.toLowerCase() === userIn.toLowerCase());
  
  if (exists) {
    alert('이미 사용 중인 아이디입니다.');
    return;
  }

  const newUser = {
    username: userIn,
    password: passIn,
    role: 'user',
    avatar: avatarUrl,
    joinedAt: new Date().toISOString().split('T')[0]
  };

  users.push(newUser);
  VibeDB.set(VIBE_DB_KEYS.USERS, users);
  
  showToast('회원가입이 완료되었습니다! 로그인 해 주세요.');
  
  // Switch to Login Tab
  document.getElementById('tab-login-btn').click();
  document.getElementById('login-username').value = userIn;
  document.getElementById('login-password').value = '';
}

// Handles user login
function handleLoginSubmit() {
  const userIn = document.getElementById('login-username').value.trim();
  const passIn = document.getElementById('login-password').value;

  const users = VibeDB.get(VIBE_DB_KEYS.USERS) || [];
  const match = users.find(u => u.username === userIn && u.password === passIn);

  if (!match) {
    alert('아이디 또는 비밀번호가 일치하지 않습니다.');
    return;
  }

  AppState.currentUser = {
    username: match.username,
    role: match.role,
    avatar: match.avatar
  };

  VibeDB.set(VIBE_DB_KEYS.SESSION, AppState.currentUser);
  updateHeaderUserWidget();
  closeAuthDialog();
  
  showToast(`${match.username}님, 환영합니다!`);
  
  // Reload current view
  showPage(AppState.activePage);
  updateNotificationCenterBadge();
}

function handleLogout() {
  if (confirm('로그아웃 하시겠습니까?')) {
    AppState.currentUser = null;
    localStorage.removeItem(VIBE_DB_KEYS.SESSION);
    updateHeaderUserWidget();
    showToast('안전하게 로그아웃 되었습니다.');
    showPage('feed');
  }
}

// ==========================================
// 4. MUSIC LIBRARY & YOUTUBE PARSING
// ==========================================

// Regular expression to parse YouTube URL/Video ID
function extractYouTubeId(urlOrId) {
  const cleaned = urlOrId.trim();
  if (cleaned.length === 11) return cleaned;
  
  const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
  const match = cleaned.match(regExp);
  return (match && match[2].length === 11) ? match[2] : null;
}

const INVIDIOUS_INSTANCES = [
  'https://yewtu.be',
  'https://vid.puffyan.us',
  'https://invidious.nerdvpn.de',
  'https://inv.tux.im',
  'https://invidious.flokinet.to',
  'https://invidious.no-logs.com'
];

// Fallback search mechanism on public Invidious API instances (No Google API key required)
async function searchYouTubeRealtime(query) {
  for (let instance of INVIDIOUS_INSTANCES) {
    try {
      const url = `${instance}/api/v1/search?q=${encodeURIComponent(query)}&type=video`;
      const controller = new AbortController();
      const id = setTimeout(() => controller.abort(), 6000); // 6s timeout per request
      
      const res = await fetch(url, { signal: controller.signal });
      clearTimeout(id);
      
      if (!res.ok) throw new Error(`HTTP error ${res.status} from ${instance}`);
      const data = await res.json();
      
      if (Array.isArray(data) && data.length > 0) {
        return data.map(item => ({
          youtubeId: item.videoId,
          title: item.title,
          desc: item.description || `${item.author}의 감성 라이브 트랙. VIBE에서 직접 감상해 보세요.`,
          author: item.author
        }));
      }
    } catch (err) {
      console.warn(`Failed search via Invidious instance (${instance}):`, err);
    }
  }
  
  // API Callbacks local database fallback if Invidious is completely blocked/offline
  console.error("All Invidious instances failed. Falling back to fuzzy local database search.");
  return searchLocalDatabaseFuzzy(query);
}

// Resilient local fallback search if all external API calls fail
function searchLocalDatabaseFuzzy(query) {
  const musicList = VibeDB.get(VIBE_DB_KEYS.MUSIC) || [];
  const qLower = query.toLowerCase();
  
  return musicList.filter(m => 
    m.title.toLowerCase().includes(qLower) || 
    m.desc.toLowerCase().includes(qLower) ||
    m.tags.some(t => t.toLowerCase().includes(qLower))
  ).map(m => ({
    youtubeId: m.youtubeId,
    title: m.title,
    desc: m.desc,
    author: m.createdBy
  }));
}

// Ingest search items dynamically into local database to support comments, likes and tags
function autoIngestYoutubeTrack(videoObj) {
  const musicList = VibeDB.get(VIBE_DB_KEYS.MUSIC) || [];
  const targetId = `yt_${videoObj.youtubeId}`;
  
  const existing = musicList.find(m => m.id === targetId || m.youtubeId === videoObj.youtubeId);
  if (existing) {
    return existing;
  }
  
  // Standardize tag from author
  const initialTag = videoObj.author ? videoObj.author.replace(/#/g, '').replace(/\s+/g, '').trim() : '유튜브';
  
  const newMusic = {
    id: targetId,
    youtubeId: videoObj.youtubeId,
    title: videoObj.title,
    desc: videoObj.desc || '아름다운 보태니컬 다크 감성의 음악 공간 VIBE.',
    tags: [initialTag].filter(t => t.length > 0),
    likes: [],
    createdBy: videoObj.author || 'YouTube',
    createdAt: new Date().toISOString()
  };
  
  musicList.unshift(newMusic);
  VibeDB.set(VIBE_DB_KEYS.MUSIC, musicList);
  
  // Refresh feed silently in background
  renderFeedPage();
  
  return newMusic;
}

// ==========================================
// 5. COMMENTS, LIKES, AND HASHTAGS
// ==========================================

function handleToggleLike(musicId, e) {
  e.stopPropagation(); // prevent card click triggers
  
  if (!AppState.currentUser) {
    showToast('좋아요를 누르려면 먼저 로그인해 주세요.');
    openAuthDialog();
    return;
  }

  const musicList = VibeDB.get(VIBE_DB_KEYS.MUSIC) || [];
  const track = musicList.find(m => m.id === musicId);
  
  if (!track) return;

  const username = AppState.currentUser.username;
  const index = track.likes.indexOf(username);

  if (index > -1) {
    // Unlike
    track.likes.splice(index, 1);
  } else {
    // Like
    track.likes.push(username);
    showToast(`"${track.title}" 곡을 좋아합니다.`);
  }

  VibeDB.set(VIBE_DB_KEYS.MUSIC, musicList);
  
  // Refresh views
  if (AppState.activeMusicDetailId === musicId) {
    updateMusicDetailModalLikes(track);
  }
  
  renderFeedPage();
  if (AppState.activePage === 'search') renderSearchPage();
  if (AppState.activePage === 'profile') renderProfilePage();
}

// Add a custom hashtag in Detail view
function handleAddHashtag() {
  if (!AppState.currentUser) {
    showToast('해시태그를 추가하려면 먼저 로그인해 주세요.');
    openAuthDialog();
    return;
  }

  const input = document.getElementById('new-tag-input');
  const rawTag = input.value.replace(/#/g, '').trim();

  if (!rawTag) return;

  const musicList = VibeDB.get(VIBE_DB_KEYS.MUSIC) || [];
  const track = musicList.find(m => m.id === AppState.activeMusicDetailId);
  
  if (!track) return;

  // Enforce hashtag uniqueness (no duplicates allowed for this song)
  if (track.tags.some(t => t.toLowerCase() === rawTag.toLowerCase())) {
    alert("이미 등록된 동일한 해시태그가 있습니다.");
    input.value = '';
    return;
  }

  track.tags.push(rawTag);
  VibeDB.set(VIBE_DB_KEYS.MUSIC, musicList);
  
  input.value = '';
  showToast(`해시태그 #${rawTag} 추가 완료!`);
  
  // Update Detail modal tag views
  renderDetailModalTags(track.tags);
  renderFeedPage();
}

// Add a live comment
function handleSubmitComment() {
  if (!AppState.currentUser) {
    showToast('의견을 나누려면 로그인해 주세요.');
    openAuthDialog();
    return;
  }

  const textIn = document.getElementById('comment-textarea-input').value.trim();
  if (!textIn) return;

  const musicId = AppState.activeMusicDetailId;
  const comments = VibeDB.get(VIBE_DB_KEYS.COMMENTS) || [];

  const newComment = {
    id: 'c_' + Date.now(),
    musicId: musicId,
    username: AppState.currentUser.username,
    avatar: AppState.currentUser.avatar || DEFAULT_AVATARS[0],
    content: textIn,
    timestamp: new Date().toISOString()
  };

  comments.push(newComment);
  VibeDB.set(VIBE_DB_KEYS.COMMENTS, comments);

  document.getElementById('comment-textarea-input').value = '';
  
  // Trigger notifications
  triggerNotificationsForComment(newComment);

  // Rerender comment section
  renderDetailModalComments(musicId);
  
  // Refresh backgrounds
  renderFeedPage();
  if (AppState.activePage === 'search') renderSearchPage();
}

// Comment deletion logic (by author or admin)
function handleDeleteComment(commentId, e) {
  e.stopPropagation();
  if (!AppState.currentUser) return;

  if (!confirm('이 댓글을 삭제하시겠습니까?')) return;

  const comments = VibeDB.get(VIBE_DB_KEYS.COMMENTS) || [];
  const comment = comments.find(c => c.id === commentId);

  if (!comment) return;

  // Only author or admin can delete
  if (comment.username !== AppState.currentUser.username && AppState.currentUser.role !== 'admin') {
    alert('삭제 권한이 없습니다.');
    return;
  }

  const updated = comments.filter(c => c.id !== commentId);
  VibeDB.set(VIBE_DB_KEYS.COMMENTS, updated);
  
  showToast('댓글이 삭제되었습니다.');

  // Refresh
  renderDetailModalComments(AppState.activeMusicDetailId);
  renderFeedPage();
  if (AppState.activePage === 'search') renderSearchPage();
  if (AppState.activePage === 'profile') renderProfilePage();
  if (AppState.activePage === 'admin') renderAdminPage();
}

// ==========================================
// 6. DYNAMIC NOTIFICATION SYSTEM
// ==========================================

/**
 * Requirement: 내가 좋아요한 음악에 남들이 댓글달면 나에게 notification이라는 곳으로 1 숫자 알림이 옴.
 * Triggers alert whenever comments are added to tracks that others liked.
 */
function triggerNotificationsForComment(comment) {
  const musicList = VibeDB.get(VIBE_DB_KEYS.MUSIC) || [];
  const track = musicList.find(m => m.id === comment.musicId);
  
  if (!track) return;

  const notifications = VibeDB.get(VIBE_DB_KEYS.NOTIFICATIONS) || [];
  const commentersName = comment.username;

  // Find all users who liked this track EXCEPT the commenter
  const eligibleUsers = track.likes.filter(username => username !== commentersName);

  eligibleUsers.forEach(targetUser => {
    const newNoti = {
      id: 'n_' + Date.now() + '_' + Math.random().toString(36).substr(2, 5),
      targetUser: targetUser,
      triggeringUser: commentersName,
      triggeringAvatar: comment.avatar,
      musicId: track.id,
      musicTitle: track.title,
      commentText: comment.content,
      read: false,
      timestamp: new Date().toISOString()
    };
    notifications.unshift(newNoti);
  });

  VibeDB.set(VIBE_DB_KEYS.NOTIFICATIONS, notifications);
  
  // If target user is online, flash a toast in real-time
  if (AppState.currentUser) {
    const isTargetOnline = eligibleUsers.includes(AppState.currentUser.username);
    if (isTargetOnline) {
      showToast(`🔔 좋아요한 곡에 새 댓글이 달렸습니다!`);
    }
  }

  updateNotificationCenterBadge();
}

// Updates bell count badge
function updateNotificationCenterBadge() {
  const badge = document.getElementById('noti-badge');
  if (!AppState.currentUser) {
    badge.classList.add('hidden');
    return;
  }

  const notifications = VibeDB.get(VIBE_DB_KEYS.NOTIFICATIONS) || [];
  const unreadCount = notifications.filter(n => n.targetUser === AppState.currentUser.username && !n.read).length;

  if (unreadCount > 0) {
    badge.classList.remove('hidden');
    badge.textContent = unreadCount;
  } else {
    badge.classList.add('hidden');
  }
}

// Render drop alert list
function renderNotificationsList() {
  const box = document.getElementById('noti-list-box');
  box.innerHTML = '';

  if (!AppState.currentUser) {
    box.innerHTML = `<div class="notification-empty">로그인 후 알림을 확인하세요.</div>`;
    return;
  }

  const notifications = VibeDB.get(VIBE_DB_KEYS.NOTIFICATIONS) || [];
  const myNotis = notifications.filter(n => n.targetUser === AppState.currentUser.username);

  if (myNotis.length === 0) {
    box.innerHTML = `<div class="notification-empty">새로운 알림이 없습니다.</div>`;
    return;
  }

  myNotis.forEach(noti => {
    const item = document.createElement('div');
    item.className = `notification-item ${!noti.read ? 'unread' : ''}`;
    
    const timeAgo = formatTimeAgo(noti.timestamp);
    
    item.innerHTML = `
      <img src="${noti.triggeringAvatar || DEFAULT_AVATARS[0]}" alt="Avatar">
      <div class="notification-text">
        <strong>${noti.triggeringUser}</strong> 님이 회원님이 좋아요한 곡 <strong>"${noti.musicTitle}"</strong>에 댓글을 남겼습니다: 
        <div style="font-style: italic; font-size:11px; margin-top:2px; color: var(--brand-secondary)">"${noti.commentText}"</div>
        <div class="notification-date">${timeAgo}</div>
      </div>
    `;

    // Click item jumps to detail screen
    item.addEventListener('click', () => {
      // Mark as read
      noti.read = true;
      VibeDB.set(VIBE_DB_KEYS.NOTIFICATIONS, notifications);
      updateNotificationCenterBadge();
      
      // Close dropdown
      document.getElementById('dropdown-notifications').classList.remove('active');
      
      // Open music detail modal
      openMusicDetailModal(noti.musicId);
    });

    box.appendChild(item);
  });
}

function handleMarkAllNotiRead() {
  if (!AppState.currentUser) return;
  
  const notifications = VibeDB.get(VIBE_DB_KEYS.NOTIFICATIONS) || [];
  notifications.forEach(n => {
    if (n.targetUser === AppState.currentUser.username) {
      n.read = true;
    }
  });

  VibeDB.set(VIBE_DB_KEYS.NOTIFICATIONS, notifications);
  updateNotificationCenterBadge();
  renderNotificationsList();
  showToast('모든 알림을 읽음으로 처리했습니다.');
}

// ==========================================
// 7. YOUTUBE IFRAME PLAYER SYNC ENGINE
// ==========================================

let YTPlayer = null;
let playbackTimer = null;

// Callback triggered by official iframe script loader
window.onYouTubeIframeAPIReady = function() {
  initGlobalYouTubePlayer();
};

function initGlobalYouTubePlayer() {
  // Create a persistent hidden div inside pip video panel
  const body = document.getElementById('pip-video-body');
  body.innerHTML = '<div id="yt-hidden-player-div"></div>';

  YTPlayer = new YT.Player('yt-hidden-player-div', {
    height: '100%',
    width: '100%',
    videoId: '',
    playerVars: {
      autoplay: 0,
      controls: 1,
      rel: 0,
      showinfo: 0,
      modestbranding: 1
    },
    events: {
      onReady: onYTPlayerReady,
      onStateChange: onYTPlayerStateChange
    }
  });
}

function onYTPlayerReady(e) {
  // Set default initial volume from slider
  const volumeSlider = document.getElementById('player-volume');
  YTPlayer.setVolume(volumeSlider.value);
}

function onYTPlayerStateChange(e) {
  const playIcon = document.getElementById('play-icon-svg');
  const wave = document.getElementById('player-visualizer-wave');

  if (e.data === YT.PlayerState.PLAYING) {
    playIcon.innerHTML = `<rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect>`;
    wave.classList.add('playing');
    startPlaybackProgressTracker();
  } else {
    playIcon.innerHTML = `<polygon points="5 3 19 12 5 21 5 3"></polygon>`;
    wave.classList.remove('playing');
    stopPlaybackProgressTracker();
  }
}

// Control play states
function handleTogglePlay() {
  if (!YTPlayer || !AppState.currentPlayingTrack) return;
  
  const state = YTPlayer.getPlayerState();
  if (state === YT.PlayerState.PLAYING) {
    YTPlayer.pauseVideo();
  } else {
    YTPlayer.playVideo();
  }
}

function handlePlayMusic(musicItem) {
  if (!YTPlayer) return;

  AppState.currentPlayingTrack = musicItem;

  // Load and play video ID
  YTPlayer.loadVideoById(musicItem.youtubeId);
  YTPlayer.playVideo();

  // Update Player Deck UI
  document.getElementById('player-thumb').src = `https://img.youtube.com/vi/${musicItem.youtubeId}/hqdefault.jpg`;
  document.getElementById('player-title').textContent = musicItem.title;
  document.getElementById('player-desc').textContent = musicItem.desc;

  showToast(`재생 중: ${musicItem.title}`);
}

function handleNextTrack() {
  if (AppState.playlist.length === 0) return;
  const currentIdx = AppState.playlist.findIndex(m => m.id === AppState.currentPlayingTrack?.id);
  
  let nextIdx = 0;
  if (currentIdx > -1 && currentIdx < AppState.playlist.length - 1) {
    nextIdx = currentIdx + 1;
  }
  handlePlayMusic(AppState.playlist[nextIdx]);
}

function handlePrevTrack() {
  if (AppState.playlist.length === 0) return;
  const currentIdx = AppState.playlist.findIndex(m => m.id === AppState.currentPlayingTrack?.id);
  
  let prevIdx = AppState.playlist.length - 1;
  if (currentIdx > 0) {
    prevIdx = currentIdx - 1;
  }
  handlePlayMusic(AppState.playlist[prevIdx]);
}

// Seeker Progress Tracker
function startPlaybackProgressTracker() {
  stopPlaybackProgressTracker();
  playbackTimer = setInterval(() => {
    if (!YTPlayer || !YTPlayer.getCurrentTime) return;
    
    const curr = YTPlayer.getCurrentTime() || 0;
    const dur = YTPlayer.getDuration() || 0;
    
    if (dur > 0) {
      const pct = (curr / dur) * 100;
      document.getElementById('player-slider-fill').style.width = `${pct}%`;
      document.getElementById('player-time-current').textContent = formatSecondsToMMSS(curr);
      document.getElementById('player-time-total').textContent = formatSecondsToMMSS(dur);
    }
  }, 500);
}

function stopPlaybackProgressTracker() {
  if (playbackTimer) {
    clearInterval(playbackTimer);
    playbackTimer = null;
  }
}

// Click and Seek inside timeline bar
function handleSeekPlayback(e) {
  if (!YTPlayer || !YTPlayer.getDuration || !AppState.currentPlayingTrack) return;
  
  const container = document.getElementById('player-slider-container');
  const rect = container.getBoundingClientRect();
  const clickX = e.clientX - rect.left;
  const totalWidth = rect.width;
  
  const pct = Math.max(0, Math.min(1, clickX / totalWidth));
  const seekTime = pct * YTPlayer.getDuration();
  
  YTPlayer.seekTo(seekTime, true);
  document.getElementById('player-slider-fill').style.width = `${pct * 100}%`;
  document.getElementById('player-time-current').textContent = formatSecondsToMMSS(seekTime);
}

// Volume Controls
function handleVolumeChange(e) {
  if (YTPlayer && YTPlayer.setVolume) {
    YTPlayer.setVolume(e.target.value);
  }
}

// Picture in Picture View Manager
function togglePipVideoPanel() {
  const panel = document.getElementById('pip-video-panel');
  const btn = document.getElementById('btn-toggle-pip');
  
  const active = panel.classList.toggle('active');
  btn.classList.toggle('active', active);

  if (active) {
    showToast('비디오 미니 윈도우가 활성화되었습니다.');
  }
}

// ==========================================
// 8. DYNAMIC PAGE RENDERERS
// ==========================================

// Helper functions for relative dates and conversions
function formatSecondsToMMSS(secs) {
  const m = Math.floor(secs / 60);
  const s = Math.floor(secs % 60);
  return `${m}:${s < 10 ? '0' : ''}${s}`;
}

function formatTimeAgo(isoString) {
  const d = new Date(isoString);
  const diffMs = Date.now() - d.getTime();
  const diffMins = Math.floor(diffMs / 60000);
  
  if (diffMins < 1) return '방금 전';
  if (diffMins < 60) return `${diffMins}분 전`;
  
  const diffHrs = Math.floor(diffMins / 60);
  if (diffHrs < 24) return `${diffHrs}시간 전`;
  
  return isoString.split('T')[0];
}

// A. RENDER PAGE 1: FEED
function renderFeedPage() {
  const musicList = VibeDB.get(VIBE_DB_KEYS.MUSIC) || [];
  AppState.playlist = [...musicList]; // feed forms the playing queue

  // 1. Build Tag Quick Filters on Feed Top
  const tagBox = document.getElementById('feed-tags-quick');
  const allTags = musicList.reduce((acc, track) => [...acc, ...track.tags], []);
  
  // Count frequency of hashtags
  const tagCounts = {};
  allTags.forEach(t => tagCounts[t] = (tagCounts[t] || 0) + 1);

  // Sort unique hashtags
  const sortedTags = Object.keys(tagCounts).sort((a,b) => tagCounts[b] - tagCounts[a]);

  // Keep a selected filter state if active
  const prevActiveTag = tagBox.querySelector('.filter-btn.active')?.dataset.tag || 'all';

  tagBox.innerHTML = `
    <button class="filter-btn ${prevActiveTag === 'all' ? 'active' : ''}" data-tag="all">전체보기 (${musicList.length})</button>
  `;

  sortedTags.slice(0, 10).forEach(tag => {
    const btn = document.createElement('button');
    btn.className = `filter-btn ${prevActiveTag === tag ? 'active' : ''}`;
    btn.dataset.tag = tag;
    btn.textContent = `#${tag} (${tagCounts[tag]})`;
    
    btn.addEventListener('click', () => {
      tagBox.querySelectorAll('.filter-btn').forEach(el => el.classList.remove('active'));
      btn.classList.add('active');
      filterFeedByTag(tag);
    });

    tagBox.appendChild(btn);
  });

  // Re-bind click for "all" filter
  tagBox.querySelector('[data-tag="all"]').addEventListener('click', (e) => {
    tagBox.querySelectorAll('.filter-btn').forEach(el => el.classList.remove('active'));
    e.target.classList.add('active');
    filterFeedByTag('all');
  });

  // Render Music grid Cards (defaults to showing 'all' or active tag)
  filterFeedByTag(prevActiveTag);
}

function filterFeedByTag(tag) {
  const grid = document.getElementById('feed-music-grid');
  grid.innerHTML = '';

  const musicList = VibeDB.get(VIBE_DB_KEYS.MUSIC) || [];
  let filtered = musicList;

  const titleEl = document.getElementById('feed-music-title');
  if (tag !== 'all') {
    filtered = musicList.filter(m => m.tags.includes(tag));
    titleEl.textContent = `#${tag} 해시태그 게시글 (${filtered.length})`;
  } else {
    titleEl.textContent = `모든 공유 음악 (${filtered.length})`;
  }

  if (filtered.length === 0) {
    grid.innerHTML = `<div style="grid-column: 1/-1; text-align: center; color: var(--text-secondary); padding: 48px 0;">이 해시태그에 등록된 음악이 없습니다.</div>`;
    return;
  }

  filtered.forEach(track => {
    grid.appendChild(createMusicCardDOM(track));
  });
}

// B. RENDER PAGE 2: ADVANCED SEARCH
async function renderSearchPage(query = '') {
  const searchResultsGrid = document.getElementById('search-music-grid');
  const titleEl = document.getElementById('search-results-title');
  const subtitleEl = document.getElementById('search-page-subtitle');
  
  if (!searchResultsGrid) return;
  searchResultsGrid.innerHTML = '';
  
  if (!query) {
    // Show default community library tracks when search query is empty
    const musicList = VibeDB.get(VIBE_DB_KEYS.MUSIC) || [];
    if (titleEl) titleEl.textContent = `추천 음악 라이브러리 (${musicList.length}곡)`;
    if (subtitleEl) subtitleEl.textContent = `상단 검색창을 통해 유튜브 음악을 실시간으로 탐색해 보세요.`;
    
    if (musicList.length === 0) {
      searchResultsGrid.innerHTML = `<div style="grid-column: 1/-1; text-align: center; color: var(--text-secondary); padding: 48px 0;">등록된 음악이 없습니다.</div>`;
      return;
    }
    musicList.forEach(track => {
      searchResultsGrid.appendChild(createMusicCardDOM(track));
    });
    return;
  }
  
  // Render luxurious skeleton loading states during API call
  if (titleEl) titleEl.textContent = `"${query}" 유튜브 실시간 탐색 중...`;
  if (subtitleEl) subtitleEl.textContent = `유튜브 전 세계 라이브 비디오 트랙을 수집하고 있습니다.`;
  
  for (let i = 0; i < 8; i++) {
    const skeleton = document.createElement('div');
    skeleton.className = 'skeleton-card';
    skeleton.innerHTML = `
      <div class="skeleton-thumbnail"></div>
      <div class="skeleton-body">
        <div class="skeleton-title"></div>
        <div class="skeleton-desc"></div>
        <div class="skeleton-footer"></div>
      </div>
    `;
    searchResultsGrid.appendChild(skeleton);
  }
  
  // Dynamic API Fetching
  const results = await searchYouTubeRealtime(query);
  searchResultsGrid.innerHTML = '';
  
  if (results.length === 0) {
    if (titleEl) titleEl.textContent = `"${query}" 결과 없음`;
    searchResultsGrid.innerHTML = `<div style="grid-column: 1/-1; text-align: center; color: var(--text-secondary); padding: 48px 0;">유튜브 실시간 검색 결과가 없습니다. 다른 단어로 검색해 보세요.</div>`;
    return;
  }
  
  if (titleEl) titleEl.textContent = `유튜브 실시간 검색 결과 (${results.length}곡)`;
  if (subtitleEl) subtitleEl.textContent = `클릭/재생 시 자동으로 곡 정보가 등록되어 자유롭게 댓글 및 좋아요 소통이 가능합니다.`;
  
  results.forEach(video => {
    // Cross-match with local database to see if already ingested
    const musicList = VibeDB.get(VIBE_DB_KEYS.MUSIC) || [];
    const existing = musicList.find(m => m.youtubeId === video.youtubeId);
    
    const displayTrack = existing || {
      id: `temp_${video.youtubeId}`,
      youtubeId: video.youtubeId,
      title: video.title,
      desc: video.desc,
      tags: [video.author ? video.author.replace(/#/g, '').replace(/\s+/g, '').trim() : '유튜브'].filter(t => t.length > 0),
      likes: [],
      createdBy: video.author || 'YouTube',
      createdAt: new Date().toISOString()
    };
    
    searchResultsGrid.appendChild(createRealtimeMusicCardDOM(displayTrack, video));
  });
}

// Reusable card DOM generator for local database tracks (Feed Page)
function createMusicCardDOM(track) {
  const card = document.createElement('div');
  card.className = 'music-card';

  const isLiked = AppState.currentUser ? track.likes.includes(AppState.currentUser.username) : false;
  const comments = VibeDB.get(VIBE_DB_KEYS.COMMENTS) || [];
  const comCount = comments.filter(c => c.musicId === track.id).length;

  card.innerHTML = `
    <div class="music-card-thumbnail">
      <img src="https://img.youtube.com/vi/${track.youtubeId}/hqdefault.jpg" alt="Thumbnail">
      <button class="music-card-play-btn" title="재생">
        <svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
      </button>
    </div>
    
    <div class="music-card-body">
      <h3 class="music-card-title" title="${track.title}">${track.title}</h3>
      <p class="music-card-desc">${track.desc}</p>
      
      <div class="music-card-tags">
        ${track.tags.map(t => `<span class="tag-badge">#${t}</span>`).join('')}
      </div>

      <div class="music-card-footer">
        <div class="card-actions">
          <button class="card-action-btn ${isLiked ? 'liked' : ''}" data-action="like" title="좋아요 토글">
            <svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
            <span class="like-num">${track.likes.length}</span>
          </button>
          
          <button class="card-action-btn" data-action="comments" title="댓글 보기">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
            </svg>
            <span>${comCount}</span>
          </button>
        </div>

        <span class="card-uploader">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
          ${track.createdBy}
        </span>
      </div>
    </div>
  `;

  // Bind clicks
  card.querySelector('.music-card-play-btn').addEventListener('click', (e) => {
    e.stopPropagation();
    handlePlayMusic(track);
  });

  card.querySelector('[data-action="like"]').addEventListener('click', (e) => {
    handleToggleLike(track.id, e);
  });

  // Hashtag badges click triggers search view
  card.querySelectorAll('.tag-badge').forEach(badge => {
    badge.addEventListener('click', (e) => {
      e.stopPropagation();
      const rawText = badge.textContent.replace('#', '');
      document.getElementById('global-search-input').value = rawText;
      showPage('search');
    });
  });

  // Open modal details
  card.addEventListener('click', () => {
    openMusicDetailModal(track.id);
  });

  return card;
}

// Special Realtime-Search Card Generator that runs Auto-Ingestion on interaction
function createRealtimeMusicCardDOM(displayTrack, originalVideo) {
  const card = document.createElement('div');
  card.className = 'music-card';

  const isLiked = AppState.currentUser ? displayTrack.likes.includes(AppState.currentUser.username) : false;
  const comments = VibeDB.get(VIBE_DB_KEYS.COMMENTS) || [];
  const comCount = comments.filter(c => c.musicId === displayTrack.id).length;

  card.innerHTML = `
    <div class="music-card-thumbnail">
      <img src="https://img.youtube.com/vi/${displayTrack.youtubeId}/hqdefault.jpg" alt="Thumbnail">
      <button class="music-card-play-btn" title="재생">
        <svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
      </button>
    </div>
    
    <div class="music-card-body">
      <h3 class="music-card-title" title="${displayTrack.title}">${displayTrack.title}</h3>
      <p class="music-card-desc">${displayTrack.desc}</p>
      
      <div class="music-card-tags">
        ${displayTrack.tags.map(t => `<span class="tag-badge">#${t}</span>`).join('')}
      </div>

      <div class="music-card-footer">
        <div class="card-actions">
          <button class="card-action-btn ${isLiked ? 'liked' : ''}" data-action="like" title="좋아요 토글">
            <svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
            <span class="like-num">${displayTrack.likes.length}</span>
          </button>
          
          <button class="card-action-btn" data-action="comments" title="댓글 보기">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
            </svg>
            <span>${comCount}</span>
          </button>
        </div>

        <span class="card-uploader">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
          ${displayTrack.createdBy}
        </span>
      </div>
    </div>
  `;

  // Auto-Ingest and then Play
  card.querySelector('.music-card-play-btn').addEventListener('click', (e) => {
    e.stopPropagation();
    const ingested = autoIngestYoutubeTrack(originalVideo);
    handlePlayMusic(ingested);
  });

  // Auto-Ingest and then Like
  card.querySelector('[data-action="like"]').addEventListener('click', (e) => {
    e.stopPropagation();
    const ingested = autoIngestYoutubeTrack(originalVideo);
    handleToggleLike(ingested.id, e);
  });

  // Hashtag badge search triggers
  card.querySelectorAll('.tag-badge').forEach(badge => {
    badge.addEventListener('click', (e) => {
      e.stopPropagation();
      autoIngestYoutubeTrack(originalVideo);
      const rawText = badge.textContent.replace('#', '');
      document.getElementById('global-search-input').value = rawText;
      showPage('search');
    });
  });

  // Auto-Ingest and then Open Details Modal
  card.addEventListener('click', () => {
    const ingested = autoIngestYoutubeTrack(originalVideo);
    openMusicDetailModal(ingested.id);
  });

  return card;
}

// C. RENDER PAGE 3: MY PROFILE
function renderProfilePage() {
  const wrapper = document.getElementById('profile-details-wrapper');
  
  if (!AppState.currentUser) {
    wrapper.innerHTML = `
      <div style="grid-column: 1/-1; text-align: center; padding: 48px;">
        <div class="alert-box flex-center" style="max-width: 500px; margin: 0 auto;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          로그인하시면 나만의 스페이스에서 작성한 의견과 좋아요 기록을 모아 볼 수 있습니다.
        </div>
        <button class="btn-login" id="profile-login-trigger" style="margin-top: 24px;">로그인하기</button>
      </div>
    `;
    document.getElementById('profile-login-trigger').addEventListener('click', openAuthDialog);
    return;
  }

  const username = AppState.currentUser.username;
  const musicList = VibeDB.get(VIBE_DB_KEYS.MUSIC) || [];
  const comments = VibeDB.get(VIBE_DB_KEYS.COMMENTS) || [];

  // Calculate user stats
  const commentsWritten = comments.filter(c => c.username === username);
  const likedSongs = musicList.filter(m => m.likes.includes(username));
  const likedSongsCount = likedSongs.length;

  // Build Profile DOM
  let commentsTimelineHTML = '';
  if (commentsWritten.length === 0) {
    commentsTimelineHTML = `<div class="timeline-empty">작성하신 코멘트 의견이 아직 없습니다. 음악에 영감을 달아보세요!</div>`;
  } else {
    // Reverse timeline (most recent first)
    const reversed = [...commentsWritten].reverse();
    reversed.forEach(c => {
      const parentTrack = musicList.find(m => m.id === c.musicId);
      if (!parentTrack) return;
      
      const timeAgo = formatTimeAgo(c.timestamp);
      commentsTimelineHTML += `
        <div class="timeline-item" data-music-id="${c.musicId}">
          <img src="https://img.youtube.com/vi/${parentTrack.youtubeId}/hqdefault.jpg" alt="Track" class="timeline-track-thumb">
          <div class="timeline-detail">
            <div class="timeline-track-title">${parentTrack.title}</div>
            <div class="timeline-comment-text">"${c.content}"</div>
            <div class="timeline-time">${timeAgo}</div>
          </div>
        </div>
      `;
    });
  }

  let likedSongsHTML = '';
  if (likedSongsCount === 0) {
    likedSongsHTML = `<div class="timeline-empty">좋아요를 누른 음악이 없습니다. 마음에 드는 곡을 보관해 보세요!</div>`;
  } else {
    likedSongs.forEach(track => {
      likedSongsHTML += `
        <div class="timeline-item" data-music-id="${track.id}">
          <img src="https://img.youtube.com/vi/${track.youtubeId}/hqdefault.jpg" alt="Track" class="timeline-track-thumb">
          <div class="timeline-detail">
            <div class="timeline-track-title">${track.title}</div>
            <div class="timeline-comment-text">${track.desc}</div>
            <div class="timeline-time">${track.likes.length}명이 좋아하는 곡</div>
          </div>
        </div>
      `;
    });
  }

  wrapper.innerHTML = `
    <!-- User summary info -->
    <div class="profile-sidebar">
      <img src="${AppState.currentUser.avatar || DEFAULT_AVATARS[0]}" alt="Avatar" class="profile-avatar-big">
      <h2 class="profile-username">${username}</h2>
      <span class="profile-role-badge">${AppState.currentUser.role === 'admin' ? '관리자 권한' : '커뮤니티 회원'}</span>
      
      <div class="profile-stats">
        <div class="stat-item">
          <span class="stat-value">${commentsWritten.length}</span>
          <span class="stat-label">작성한 댓글</span>
        </div>
        <div class="stat-item" style="border-left: 1px solid var(--border-subtle); padding-left: 20px;">
          <span class="stat-value">${likedSongsCount}</span>
          <span class="stat-label">좋아요 누른 곡</span>
        </div>
      </div>

      <button class="btn-logout" id="btn-profile-logout">로그아웃</button>
    </div>

    <!-- Timeline of Comments & Likes -->
    <div class="profile-content">
      <div style="margin-bottom: 40px;">
        <h3 class="profile-section-title">내가 작성한 댓글 피드</h3>
        <div class="timeline-list">
          ${commentsTimelineHTML}
        </div>
      </div>
      
      <div>
        <h3 class="profile-section-title">내가 좋아요 한 음악 목록</h3>
        <div class="timeline-list">
          ${likedSongsHTML}
        </div>
      </div>
    </div>
  `;

  // Bind actions
  document.getElementById('btn-profile-logout').addEventListener('click', handleLogout);
  
  wrapper.querySelectorAll('.timeline-item').forEach(item => {
    item.addEventListener('click', () => {
      openMusicDetailModal(item.dataset.musicId);
    });
  });
}

// D. RENDER PAGE 4: ADMIN DASHBOARD
function renderAdminPage() {
  if (!AppState.currentUser || AppState.currentUser.role !== 'admin') {
    document.getElementById('page-admin').innerHTML = `
      <h1 class="page-title">보안 접근 차단</h1>
      <div class="alert-box flex-center" style="max-width: 500px; margin: 40px auto 0;">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
        관리자 계정 세션이 감지되지 않았습니다. 메인 화면으로 돌아가거나 관리자로 로그인 하십시오.
      </div>
    `;
    return;
  }

  // Handle panel tab visibility toggling
  document.querySelectorAll('.admin-tab-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.tab === AppState.adminActiveTab);
  });
  
  document.querySelectorAll('.admin-panel').forEach(panel => {
    panel.classList.toggle('active', panel.id === `admin-panel-${AppState.adminActiveTab}`);
  });

  // Render specific tab contents
  if (AppState.adminActiveTab === 'members') {
    renderAdminMembersTab();
  } else if (AppState.adminActiveTab === 'posts') {
    renderAdminPostsTab();
  } else if (AppState.adminActiveTab === 'comments') {
    renderAdminCommentsTab();
  }
}

// Tab 1: Member Moderator View
function renderAdminMembersTab() {
  const tbody = document.getElementById('admin-users-tbody');
  tbody.innerHTML = '';

  const users = VibeDB.get(VIBE_DB_KEYS.USERS) || [];

  users.forEach(user => {
    const tr = document.createElement('tr');
    
    // Check if self to prevent deleting self
    const isSelf = user.username === AppState.currentUser.username;
    
    tr.innerHTML = `
      <td>
        <div class="admin-user-cell">
          <img src="${user.avatar || DEFAULT_AVATARS[0]}" alt="Avatar">
          <strong>${user.username}</strong>
        </div>
      </td>
      <td>${user.username}</td>
      <td>${user.joinedAt || '2026-05-01'}</td>
      <td>
        <span class="badge-role ${user.role}">${user.role === 'admin' ? 'ADMIN' : 'USER'}</span>
      </td>
      <td>
        <div class="action-btn-group">
          ${!isSelf ? `
            <button class="admin-action-btn promote" data-action="role" data-user="${user.username}">
              ${user.role === 'admin' ? '일반회원 강등' : '관리자 승격'}
            </button>
            <button class="admin-action-btn delete" data-action="delete" data-user="${user.username}">
              추방
            </button>
          ` : '<span style="color: var(--text-tertiary);">나 (로그인 상태)</span>'}
        </div>
      </td>
    `;

    // Bind roles toggling
    const roleBtn = tr.querySelector('[data-action="role"]');
    if (roleBtn) {
      roleBtn.addEventListener('click', () => {
        const targetUser = users.find(u => u.username === user.username);
        targetUser.role = targetUser.role === 'admin' ? 'user' : 'admin';
        VibeDB.set(VIBE_DB_KEYS.USERS, users);
        showToast(`${user.username}님의 권한이 변경되었습니다.`);
        renderAdminMembersTab();
      });
    }

    // Bind block/delete user
    const delBtn = tr.querySelector('[data-action="delete"]');
    if (delBtn) {
      delBtn.addEventListener('click', () => {
        if (confirm(`진짜로 ${user.username} 회원을 영구 탈퇴시키겠습니까?`)) {
          const filtered = users.filter(u => u.username !== user.username);
          VibeDB.set(VIBE_DB_KEYS.USERS, filtered);
          
          // Also cleanup posts / likes? (Keep it simple: just remove user account)
          showToast(`${user.username} 회원이 삭제되었습니다.`);
          renderAdminMembersTab();
        }
      });
    }

    tbody.appendChild(tr);
  });
}

// Tab 2: Music posts moderator view
function renderAdminPostsTab() {
  const tbody = document.getElementById('admin-posts-tbody');
  tbody.innerHTML = '';

  const musicList = VibeDB.get(VIBE_DB_KEYS.MUSIC) || [];

  musicList.forEach(track => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>
        <img src="https://img.youtube.com/vi/${track.youtubeId}/hqdefault.jpg" alt="Thumb" style="width: 80px; aspect-ratio:16/9; border-radius: 4px; object-fit: cover;">
      </td>
      <td><strong>${track.title}</strong></td>
      <td style="max-width: 250px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${track.desc}</td>
      <td>
        <div style="display:flex; flex-wrap:wrap; gap:4px;">
          ${track.tags.map(t => `<span class="tag-badge" style="font-size:10px; padding:1px 4px;">#${t}</span>`).join('')}
        </div>
      </td>
      <td>
        <div class="action-btn-group">
          <button class="admin-action-btn edit" data-action="edit" data-id="${track.id}">수정</button>
          <button class="admin-action-btn delete" data-action="delete" data-id="${track.id}">삭제</button>
        </div>
      </td>
    `;

    // Bind Edit Post (Simple prompt dialog)
    tr.querySelector('[data-action="edit"]').addEventListener('click', () => {
      const newTitle = prompt("수정할 노래 제목:", track.title);
      if (newTitle === null) return;
      const newDesc = prompt("수정할 노래 설명:", track.desc);
      if (newDesc === null) return;
      
      const newTagsStr = prompt("수정할 해시태그 (쉼표 구분):", track.tags.join(','));
      if (newTagsStr === null) return;

      const newTags = newTagsStr.split(',')
        .map(t => t.trim())
        .filter(t => t.length > 0)
        .reduce((uniq, el) => uniq.includes(el) ? uniq : [...uniq, el], []);

      // Save
      const dbMusic = VibeDB.get(VIBE_DB_KEYS.MUSIC) || [];
      const item = dbMusic.find(m => m.id === track.id);
      if (item) {
        item.title = newTitle;
        item.desc = newDesc;
        item.tags = newTags;
        VibeDB.set(VIBE_DB_KEYS.MUSIC, dbMusic);
        showToast('음악 게시글 정보가 수정되었습니다.');
        renderAdminPostsTab();
        renderFeedPage();
      }
    });

    // Bind Delete Post
    tr.querySelector('[data-action="delete"]').addEventListener('click', () => {
      if (confirm(`"${track.title}" 음악 카드를 삭제하시겠습니까? 관련 댓글도 모두 정리됩니다.`)) {
        const dbMusic = VibeDB.get(VIBE_DB_KEYS.MUSIC) || [];
        const filteredMusic = dbMusic.filter(m => m.id !== track.id);
        VibeDB.set(VIBE_DB_KEYS.MUSIC, filteredMusic);

        // Cleanup comments
        const comments = VibeDB.get(VIBE_DB_KEYS.COMMENTS) || [];
        const filteredComments = comments.filter(c => c.musicId !== track.id);
        VibeDB.set(VIBE_DB_KEYS.COMMENTS, filteredComments);

        showToast('음악 게시글이 안전하게 정리되었습니다.');
        renderAdminPostsTab();
        renderFeedPage();
      }
    });

    tbody.appendChild(tr);
  });
}

// Tab 3: Comments Moderator View
function renderAdminCommentsTab() {
  const tbody = document.getElementById('admin-comments-tbody');
  tbody.innerHTML = '';

  const comments = VibeDB.get(VIBE_DB_KEYS.COMMENTS) || [];
  const musicList = VibeDB.get(VIBE_DB_KEYS.MUSIC) || [];

  if (comments.length === 0) {
    tbody.innerHTML = `<tr><td colspan="5" style="text-align: center; color: var(--text-tertiary);">등록된 댓글 소통이 아직 없습니다.</td></tr>`;
    return;
  }

  // Display comments in chronological order (most recent first)
  const sorted = [...comments].reverse();

  sorted.forEach(comment => {
    const parentTrack = musicList.find(m => m.id === comment.musicId);
    const trackTitle = parentTrack ? parentTrack.title : `삭제된 음악 (ID: ${comment.musicId})`;

    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td style="max-width: 150px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; color: var(--brand-primary)">
        <strong>${trackTitle}</strong>
      </td>
      <td>
        <span style="font-weight: 500">${comment.username}</span>
      </td>
      <td style="max-width: 300px; word-break: break-all;">${comment.content}</td>
      <td>${formatTimeAgo(comment.timestamp)}</td>
      <td>
        <button class="admin-action-btn delete" data-action="delete" data-id="${comment.id}">삭제</button>
      </td>
    `;

    // Bind Comments Deletion in panel
    tr.querySelector('[data-action="delete"]').addEventListener('click', (e) => {
      handleDeleteComment(comment.id, e);
    });

    tbody.appendChild(tr);
  });
}

// ==========================================
// 9. OVERLAY MODALS RENDERING (Music Details)
// ==========================================

function openMusicDetailModal(musicId) {
  AppState.activeMusicDetailId = musicId;
  const musicList = VibeDB.get(VIBE_DB_KEYS.MUSIC) || [];
  const track = musicList.find(m => m.id === musicId);

  if (!track) return;

  const modal = document.getElementById('music-detail-modal');
  modal.style.display = 'flex';
  setTimeout(() => modal.classList.add('active'), 10);

  // Set titles
  document.getElementById('modal-track-title').textContent = track.title;
  document.getElementById('modal-track-desc').textContent = track.desc;

  // Uploader avatar information
  const users = VibeDB.get(VIBE_DB_KEYS.USERS) || [];
  const uploader = users.find(u => u.username === track.createdBy);
  document.getElementById('modal-uploader-name').textContent = track.createdBy;
  document.getElementById('modal-uploader-avatar').src = uploader?.avatar || DEFAULT_AVATARS[0];

  // Injected playable YouTube Player embedded view
  const playerWrapper = document.getElementById('iframe-player-wrapper');
  
  // UX Optimization: If the current track is already loaded in the global player deck, we can let user view it, 
  // or we can embed a dedicated player in the modal. But to avoid disrupting active audio background play, 
  // we can load the iframe directly inside the modal's container when details are opened. 
  // That lets them watch/hear clearly! 
  playerWrapper.innerHTML = `
    <iframe src="https://www.youtube.com/embed/${track.youtubeId}?autoplay=1&enablejsapi=1&rel=0" 
            allow="autoplay; encrypted-media" 
            allowfullscreen></iframe>
  `;

  // Sync Likes
  updateMusicDetailModalLikes(track);

  // Render Hashtags editor
  renderDetailModalTags(track.tags);

  // Render live comments feed
  renderDetailModalComments(track.id);

  // Comments Auth input gating toggle
  const formBox = document.getElementById('comment-form-panel');
  const hintBox = document.getElementById('comment-login-hint');

  if (AppState.currentUser) {
    formBox.classList.remove('hidden');
    hintBox.classList.add('hidden');
  } else {
    formBox.classList.add('hidden');
    hintBox.classList.remove('hidden');
  }
}

function closeMusicDetailModal() {
  const modal = document.getElementById('music-detail-modal');
  modal.classList.remove('active');
  setTimeout(() => {
    modal.style.display = 'none';
    // Clear detail iframe to stop video playing on close
    document.getElementById('iframe-player-wrapper').innerHTML = '';
  }, 300);

  AppState.activeMusicDetailId = null;
}

function updateMusicDetailModalLikes(track) {
  const likeBtn = document.getElementById('modal-btn-like');
  const countEl = document.getElementById('modal-like-count');
  
  countEl.textContent = track.likes.length;

  const isLiked = AppState.currentUser ? track.likes.includes(AppState.currentUser.username) : false;
  likeBtn.classList.toggle('liked', isLiked);
}

// Render dynamic hashtags list in modal
function renderDetailModalTags(tagsArray) {
  const tagsWrapper = document.getElementById('modal-tags-wrapper');
  tagsWrapper.innerHTML = '';

  if (tagsArray.length === 0) {
    tagsWrapper.innerHTML = `<span style="font-size:12px; color: var(--text-tertiary)">아직 등록된 태그가 없습니다.</span>`;
    return;
  }

  tagsArray.forEach(tag => {
    const badge = document.createElement('span');
    badge.className = 'tag-badge';
    badge.textContent = `#${tag}`;
    
    // Clicking tags in modal closes detail, jumps to search page with hashtag active
    badge.addEventListener('click', () => {
      closeMusicDetailModal();
      AppState.searchType = 'tag';
      document.getElementById('search-input').value = tag;
      
      document.querySelectorAll('#search-category-group .filter-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.type === 'tag');
      });

      showPage('search');
    });

    tagsWrapper.appendChild(badge);
  });
}

// Render detailed live comments list
function renderDetailModalComments(musicId) {
  const commentsWrapper = document.getElementById('modal-comments-wrapper');
  commentsWrapper.innerHTML = '';

  const comments = VibeDB.get(VIBE_DB_KEYS.COMMENTS) || [];
  const filtered = comments.filter(c => c.musicId === musicId);

  if (filtered.length === 0) {
    commentsWrapper.innerHTML = `<div class="comments-placeholder">등록된 댓글 의견이 없습니다. 첫 의견을 작성해 볼까요? 😊</div>`;
    return;
  }

  // Chronological sorting (oldest to newest)
  filtered.forEach(c => {
    const item = document.createElement('div');
    item.className = 'comment-item';

    const timeAgo = formatTimeAgo(c.timestamp);
    
    // Show deletion button only if comment is by current user or admin
    const canDelete = AppState.currentUser && (c.username === AppState.currentUser.username || AppState.currentUser.role === 'admin');

    item.innerHTML = `
      <img src="${c.avatar || DEFAULT_AVATARS[0]}" alt="Avatar" class="comment-avatar">
      <div class="comment-content">
        <div class="comment-author-bar">
          <span class="comment-author-name">${c.username}</span>
          <span class="comment-time">${timeAgo}</span>
        </div>
        <p class="comment-text">${c.content}</p>
        ${canDelete ? `
          <div style="text-align: right; margin-top:4px;">
            <button class="comment-delete-btn" data-action="delete-comment" data-id="${c.id}">삭제</button>
          </div>
        ` : ''}
      </div>
    `;

    const delBtn = item.querySelector('[data-action="delete-comment"]');
    if (delBtn) {
      delBtn.addEventListener('click', (e) => {
        handleDeleteComment(c.id, e);
      });
    }

    commentsWrapper.appendChild(item);
  });

  // Auto scroll comments to the bottom
  setTimeout(() => {
    commentsWrapper.scrollTop = commentsWrapper.scrollHeight;
  }, 100);
}

// ==========================================
// 10. SYSTEM BOOTSTRAP & DOM EVENT BINDING
// ==========================================

document.addEventListener('DOMContentLoaded', () => {

  // Setup Initial UI states
  updateHeaderUserWidget();
  updateNotificationCenterBadge();
  showPage('feed');

  // Header logo goes to main feed
  document.getElementById('logo-btn').addEventListener('click', () => {
    showPage('feed');
  });

  // Global Search Engine input binds
  const globalSearchInput = document.getElementById('global-search-input');
  if (globalSearchInput) {
    globalSearchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const q = globalSearchInput.value.trim();
        showPage('search');
        renderSearchPage(q);
      }
    });
  }

  // Admin Console gear trigger
  const adminBtn = document.getElementById('btn-admin-console');
  if (adminBtn) {
    adminBtn.addEventListener('click', () => {
      showPage('admin');
    });
  }

  // Dynamic Auth Modals Tab Switcher
  document.getElementById('tab-login-btn').addEventListener('click', (e) => {
    document.querySelectorAll('.auth-tab').forEach(t => t.classList.remove('active'));
    e.target.classList.add('active');
    document.getElementById('form-login').classList.add('active');
    document.getElementById('form-signup').classList.remove('active');
  });

  document.getElementById('tab-signup-btn').addEventListener('click', (e) => {
    document.querySelectorAll('.auth-tab').forEach(t => t.classList.remove('active'));
    e.target.classList.add('active');
    document.getElementById('form-signup').classList.add('active');
    document.getElementById('form-login').classList.remove('active');
  });

  // Authentication submission actions
  document.getElementById('btn-login-submit').addEventListener('click', handleLoginSubmit);
  document.getElementById('btn-signup-submit').addEventListener('click', handleSignUpSubmit);
  document.getElementById('btn-close-auth').addEventListener('click', closeAuthDialog);

  // Close modals clicking background
  window.addEventListener('click', (e) => {
    const authDialog = document.getElementById('auth-dialog');
    const musicDetailModal = document.getElementById('music-detail-modal');
    
    if (e.target === authDialog) closeAuthDialog();
    if (e.target === musicDetailModal) closeMusicDetailModal();
  });

  // Details Modal close
  document.getElementById('btn-close-detail-modal').addEventListener('click', closeMusicDetailModal);
  
  // Modal Hashtag click & submission
  document.getElementById('btn-add-tag-submit').addEventListener('click', handleAddHashtag);
  document.getElementById('new-tag-input').addEventListener('keydown', (e) => {
    if (e.key === 'Enter') handleAddHashtag();
  });

  // Modal Comments Submission Binds
  document.getElementById('btn-comment-submit').addEventListener('click', handleSubmitComment);
  document.getElementById('comment-textarea-input').addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmitComment();
    }
  });
  document.getElementById('link-hint-login').addEventListener('click', (e) => {
    e.preventDefault();
    closeMusicDetailModal();
    openAuthDialog();
  });

  // Notifications dropdown binder triggers
  const notiTrigger = document.getElementById('btn-notifications');
  const notiDropdown = document.getElementById('dropdown-notifications');
  
  notiTrigger.addEventListener('click', (e) => {
    e.stopPropagation();
    const active = notiDropdown.classList.toggle('active');
    if (active) {
      renderNotificationsList();
    }
  });

  // Click outside to close notifications dropdown
  window.addEventListener('click', (e) => {
    if (!notiTrigger.contains(e.target) && !notiDropdown.contains(e.target)) {
      notiDropdown.classList.remove('active');
    }
  });

  document.getElementById('btn-clear-noti').addEventListener('click', handleMarkAllNotiRead);

  // Player controls binders
  document.getElementById('player-btn-play').addEventListener('click', handleTogglePlay);
  document.getElementById('player-btn-next').addEventListener('click', handleNextTrack);
  document.getElementById('player-btn-prev').addEventListener('click', handlePrevTrack);
  
  // Volume Slider binder
  const volumeSlider = document.getElementById('player-volume');
  volumeSlider.addEventListener('input', handleVolumeChange);

  // Seek Timelines binder
  document.getElementById('player-slider-container').addEventListener('click', handleSeekPlayback);

  // Picture in Picture View triggers
  document.getElementById('btn-toggle-pip').addEventListener('click', togglePipVideoPanel);
  document.getElementById('btn-close-pip-panel').addEventListener('click', togglePipVideoPanel);
  
  // Clicking player details card jumps to details modal
  document.getElementById('player-track-card-trigger').addEventListener('click', () => {
    if (AppState.currentPlayingTrack) {
      openMusicDetailModal(AppState.currentPlayingTrack.id);
    } else {
      showToast('재생 중인 노래가 없습니다. 곡을 선택해 보세요.');
    }
  });

  // Admin tab sub-navigation click handlers
  document.querySelectorAll('.admin-tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      AppState.adminActiveTab = btn.dataset.tab;
      renderAdminPage();
    });
  });
});
