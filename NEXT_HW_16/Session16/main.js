// main.js

// 초기에 About 패널을 표시하기 위해 추가
document.getElementById('Aboutpanel').style.maxHeight = 'none';

// 각 버튼에 대한 이벤트 처리
document.getElementById('About').addEventListener('click', function () {
    togglePanel('Aboutpanel');
});

document.getElementById('Products').addEventListener('click', function () {
    togglePanel('Productspanel');
});

document.getElementById('Technology').addEventListener('click', function () {
    togglePanel('Technologypanel');
});

document.getElementById('Downloads').addEventListener('click', function () {
    togglePanel('Downloadspanel');
});

// 패널 토글 함수
function togglePanel(panelId) {
    var panel = document.getElementById(panelId);
    var buttons = document.querySelectorAll('.mybutton'); // 모든 버튼 요소 가져오기

    // 모든 패널을 닫음
    var panels = document.querySelectorAll('.panel');
    panels.forEach(function (panel) {
        panel.style.maxHeight = '0px';
    });

    // 현재 클릭한 버튼에 대응하는 패널을 열거나 닫음
    if (panel.style.maxHeight === '0px' || !panel.style.maxHeight) {
        panel.style.maxHeight = 480 + 'px'; // 패널의 실제 내용 높이로 설정
    } else {
        panel.style.maxHeight = '0px'; // 패널 숨김
    }
}

// About 버튼에 마우스를 올렸을 때의 동작
document.getElementById('About').addEventListener('mouseenter', function () {
    this.style.backgroundColor = '#ff968a'; // 마우스를 올렸을 때 배경색 변경
});

// About 버튼에서 마우스를 떼었을 때의 동작
document.getElementById('About').addEventListener('mouseleave', function () {
    this.style.backgroundColor = '#888888'; // 원래의 배경색으로 변경
});

// Products 버튼에 마우스를 올렸을 때의 동작
document.getElementById('Products').addEventListener('mouseenter', function () {
    this.style.backgroundColor = '#ffdbcc'; // 마우스를 올렸을 때 배경색 변경
});

// Products 버튼에서 마우스를 떼었을 때의 동작
document.getElementById('Products').addEventListener('mouseleave', function () {
    this.style.backgroundColor = '#888888'; // 원래의 배경색으로 변경
});

// Technology 버튼에 마우스를 올렸을 때의 동작
document.getElementById('Technology').addEventListener('mouseenter', function () {
    this.style.backgroundColor = '#a2e1db'; // 마우스를 올렸을 때 배경색 변경
});

// Technology 버튼에서 마우스를 떼었을 때의 동작
document.getElementById('Technology').addEventListener('mouseleave', function () {
    this.style.backgroundColor = '#888888'; // 원래의 배경색으로 변경
});

// Products 버튼에 마우스를 올렸을 때의 동작
document.getElementById('Downloads').addEventListener('mouseenter', function () {
    this.style.backgroundColor = '#55cbcd'; // 마우스를 올렸을 때 배경색 변경
});

// Technology 버튼에서 마우스를 떼었을 때의 동작
document.getElementById('Downloads').addEventListener('mouseleave', function () {
    this.style.backgroundColor = '#888888'; // 원래의 배경색으로 변경
});
