from functools import wraps
from datetime import datetime
from django.shortcuts import redirect

def save_access_info(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # 현재 사용자 정보 확인
        current_user = 'Anonymous'  # 기본값은 익명 사용자
        if request.user.is_authenticated:
            current_user = request.user.username

        # 현재 시간 가져오기
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 이전 사용자 정보를 세션에 저장
        request.session['last_user'] = current_user
        request.session['last_access_time'] = current_time

        # 뷰 함수 호출
        return view_func(request, *args, **kwargs)

    return wrapper
