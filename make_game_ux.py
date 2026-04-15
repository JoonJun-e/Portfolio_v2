import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the head section
head_match = re.search(r'(<head>.*?</head>)', content, re.DOTALL)
head_content = head_match.group(1) if head_match else '<head></head>'

# Add custom CSS to head before closing tag
custom_css = """
    /* Article Specific */
    .c-article {
      max-width: 900px;
      margin: 0 auto;
      padding: var(--s12) var(--s6);
      padding-top: calc(56px + var(--s12));
    }
    .c-article__title {
      font-size: var(--t-2xl);
      font-weight: 300;
      color: var(--fg-1);
      margin-bottom: var(--s6);
      line-height: 1.2;
    }
    .c-article__title span { font-weight: 500; }
    .c-article__section { margin-bottom: var(--s12); border-top: 1px solid var(--border); padding-top: var(--s8); }
    .c-article__h2 { font-size: var(--t-xl); font-weight: 500; margin-bottom: var(--s4); color: var(--fg-1); }
    .c-article__h3 { font-size: var(--t-lg); font-weight: 500; margin-bottom: var(--s3); color: var(--accent); margin-top: var(--s6); }
    .c-article__p { font-size: var(--t-md); color: var(--fg-2); line-height: 1.7; margin-bottom: var(--s4); word-break: keep-all; }
    
    .c-article__img-grid { display: grid; gap: var(--s4); margin: var(--s6) 0; }
    .c-article__img-grid--2 { grid-template-columns: 1fr 1fr; }
    .c-article__img-grid--3 { grid-template-columns: 1fr 1fr 1fr; }
    
    @media (max-width: 768px) {
      .c-article__img-grid { grid-template-columns: 1fr !important; }
    }
    
    .c-article__img { width: 100%; border: 1px solid var(--border-2); display: block; background: #000; }
    .c-article__img-caption { font-family: var(--font-mono); font-size: var(--t-xs); color: var(--fg-3); margin-top: var(--s2); text-align: center; }
    
    .c-solution-box { background: var(--surface-1); border: 1px solid var(--border-2); padding: var(--s5); margin-top: var(--s4); border-left: 3px solid var(--accent); }
    .c-solution-box-title { font-family: var(--font-mono); font-size: var(--t-xs); color: var(--accent); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: var(--s3); }
    .c-solution-box ul { list-style: none; padding: 0; }
    .c-solution-box li { padding-left: var(--s4); position: relative; margin-bottom: var(--s3); color: var(--fg-1); line-height: 1.6; }
    .c-solution-box li::before { content: '→'; position: absolute; left: 0; color: var(--accent); font-family: var(--font-mono); }
    .c-solution-box li strong { color: var(--accent-2); font-weight: 500; }
</style>
"""

head_content = head_content.replace('</style>', custom_css)
head_content = head_content.replace('<title>Choi SeongJoon — UX Researcher</title>', '<title>Game UX Analysis — Choi SeongJoon</title>')

body_content = """
<body>

  <!-- NAV -->
  <nav class="c-nav">
    <div class="c-nav__logo">
      <span class="c-nav__logo-dot"></span>
      <a href="index.html">CSJ — Portfolio</a>
    </div>
    <ul class="c-nav__links">
      <li><a href="index.html">← HOME</a></li>
    </ul>
  </nav>

  <main class="c-article">
    <h1 class="c-article__title"><span>Game UX Analysis</span><br>개선 분석 및 리포트</h1>
    
    <section class="c-article__section">
      <h2 class="c-article__h2">1. Intro: 플레이어 프로필 및 게임 이해도</h2>
      <p class="c-article__p">이 UX 분석은 단순히 겉핥기식의 리뷰가 아닙니다. 제가 직접 게임을 하드코어하게 플레이하며(길드 내 상위권, PVE 마스터 및 PVP 챌린저 티어 달성) 겪은 실제 경험을 바탕으로 작성되었습니다. 높은 플레이 타임과 게임 시스템에 대한 깊은 이해도를 기반으로, 유저들이 실제로 겪는 실질적인 페인포인트(Pain Point)를 도출했습니다.</p>
      
      <div class="c-article__img-grid c-article__img-grid--2">
        <div>
          <img src="개인 스펙(PVE마스터 및 PVP 상위권) 길드 내에서도 상위권 및 첼린져티어.PNG" alt="개인 스펙" class="c-article__img">
          <div class="c-article__img-caption">PVE 마스터 및 PVP 챌린저 티어 / 길드 내 상위권</div>
        </div>
        <div>
          <img src="길드전순위.PNG" alt="길드전 순위" class="c-article__img">
          <div class="c-article__img-caption">길드전 순위 및 활동 기록</div>
        </div>
      </div>
    </section>

    <section class="c-article__section">
      <h2 class="c-article__h2">2. 상급 결투장: 인지 부조화를 일으키는 버튼 피드백</h2>
      
      <h3 class="c-article__h3">Pain Point (문제점)</h3>
      <p class="c-article__p">상급 결투장에서는 하루에 입장권을 최대 5개까지 구매할 수 있습니다. 하지만 일일 구매 가능 횟수(5회)를 모두 소진했음에도 불구하고 <strong>‘구매 버튼’이 비활성화되지 않고 계속 클릭되는 문제</strong>가 있습니다. 유저는 버튼이 활성화되어 있기 때문에 시스템 오류로 오인하거나 계속해서 클릭을 시도하게 되며, 불필요한 조작과 유저 경험의 혼란을 야기합니다.</p>
      
      <div class="c-article__img-grid c-article__img-grid--3">
        <div>
          <img src="상급결투장 메인화면.PNG" alt="상급결투장 메인" class="c-article__img">
          <div class="c-article__img-caption">상급 결투장 메인 화면 (횟수 제한 있음)</div>
        </div>
        <div>
          <img src="상급결투장 이미 5번 다 샀는데 또 클릭됨.PNG" alt="구매 버튼 클릭됨" class="c-article__img">
          <div class="c-article__img-caption">잔여 횟수가 없어도 구매 버튼이 눌림</div>
        </div>
        <div>
          <img src="상급결투장 구매가능한횟수 초과.PNG" alt="구매가능횟수 초과" class="c-article__img">
          <div class="c-article__img-caption">눌린 이후 뒤늦게 초과 안내 등장</div>
        </div>
      </div>

      <div class="c-solution-box">
        <div class="c-solution-box-title">UX Improvement / 개선 제안</div>
        <ul>
          <li><strong>시각적 비활성화 (Disabled State 활용):</strong> 5회 구매가 완료된 시점에서 구매 버튼을 회색 처리(Dimmed)하여 직관적으로 클릭이 불가능한 상태임을 인지시킵니다. 버튼 텍스트를 '구매 완료'로 변경하는 것도 좋은 방법입니다.</li>
          <li><strong>직관적인 피드백 (Toast 팝업):</strong> 시스템 한계상 버튼을 열어두어야 한다면, 클릭 시 빈 화면이나 반응 없음이 아니라 "이미 구매를 완료했습니다"라는 짧은 토스트(Toast) 팝업을 띄워 유저에게 즉각적이고 명확한 피드백을 전달해야 합니다.</li>
        </ul>
      </div>
    </section>

    <section class="c-article__section">
      <h2 class="c-article__h2">3. 길드전: 덱 구성 화면의 사용성(Usability) 한계</h2>
      
      <h3 class="c-article__h3">Pain Point (문제점)</h3>
      <p class="c-article__p">길드전의 핵심 재미는 상대방의 덱을 분석하고 내 덱을 조합해 '카운터'를 치는 전략성에 있습니다. 이를 위해 약 50명 이상의 캐릭터 중 신중하게 선택을 해야 하는데, <strong>현재 내 캐릭터 목록이 가로 스크롤(슬라이드)로만 제공되어 덱 구성의 시야가 좁아지고 효율성이 매우 떨어집니다.</strong></p>
      <p class="c-article__p">우측의 사각형 뷰 버튼을 누르면 전체 캐릭터를 한눈에 볼 수 있지만, <strong>이 화면을 열면 상대방의 덱 정보가 완전히 가려져버리는 치명적인 단점</strong>이 발생합니다. 결국 상대 덱을 보면서 내 캐릭터를 맞춤형으로 고르는 핵심 플레이 흐름이 끊기게 됩니다.</p>

      <div class="c-article__img-grid">
        <div style="max-width:800px;">
          <img src="길드전 -카드 슬라이드 형식으로 약 50명이나 되는 캐릭터를 골라야하는 상황 상.PNG" alt="길드전 덱 설정" class="c-article__img">
          <div class="c-article__img-caption">약 50명의 캐릭터를 제한된 가로 스크롤만으로 탐색해야 하는 답답한 덱 구성 화면</div>
        </div>
      </div>

      <div class="c-solution-box">
        <div class="c-solution-box-title">UX Improvement / 개선 제안</div>
        <ul>
          <li><strong>화면 분할 및 레이아웃 재배치:</strong> 상대방의 덱 리스트를 화면 상단이나 일부분인 플로팅 영역에 고정(Sticky)시키고, 하단 영역에 내 전체 캐릭터 목록(그리드 뷰)을 띄워 <strong>'상대 덱 정보 확인'과 '내 덱 구성'이 시선 이동 없이 동시에 이루어질 수 있도록 개선</strong>해야 합니다.</li>
          <li><strong>필터링 및 정렬 도입:</strong> 좁은 영역에서 가로로 끝없이 넘기는 수고를 덜기 위해 역할군(탱커/딜러/힐러 등) 및 속성 등의 퀵 필터를 상단에 배치하여, 원하는 영웅을 빠르게 찾아 드롭할 수 있는 효율적인 동선을 구축해야 합니다.</li>
        </ul>
      </div>
    </section>

  </main>

  <footer class="c-footer">
    <span class="c-footer__copy">© 2026 Choi SeongJoon — Game UX Analysis</span>
    <div class="c-footer__links">
      <a href="index.html" class="c-footer__link">Return to Home</a>
    </div>
  </footer>

</body>
</html>
"""

full_html = f"<!DOCTYPE html>\n<html lang=\"ko\">\n{head_content}\n{body_content}"
with open('game-ux.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Generated game-ux.html successfully.")
