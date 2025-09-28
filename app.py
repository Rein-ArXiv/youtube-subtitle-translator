import logging
import os
import json
from flask import Flask, render_template, request, jsonify, Response
from dotenv import load_dotenv
from module.youtube_module import extract_youtube_transcript

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# .env 로드 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=ENV_PATH, override=False)

@app.route('/')
def index():
    """메인 페이지"""
    return render_template('index.html')

@app.route('/api/youtube/translate', methods=['POST'])
def api_youtube_translate():
    """YouTube 자막 추출 및 번역을 한 번에 처리 (YouTube 내장 번역 사용)"""
    # request context 밖에서 데이터를 미리 추출
    data = request.get_json()
    url = data.get('url')
    target_lang = data.get('target_lang', 'ko')
    
    def generate():
        try:
            if not url:
                yield json.dumps({'error': 'YouTube URL이 필요합니다.'}) + "\n"
                return
            
            # 1단계: YouTube 자막 추출 및 번역 (한 번에 처리)
            yield json.dumps({'status': 'extracting'}) + "\n"
            
            try:
                # YouTube에서 직접 목표 언어로 자막 추출 또는 번역
                extract_result = extract_youtube_transcript(url, target_lang)
                
                if not extract_result.get('success'):
                    yield json.dumps({'error': extract_result.get('error', '자막 추출 실패')}) + "\n"
                    return
                
                srt_content = extract_result['srt_content']
                video_id = extract_result['video_id']
                transcript_count = extract_result['transcript_count']
                source_info = extract_result.get('source_transcript', '알 수 없음')
                
                yield json.dumps({
                    'status': 'extracted',
                    'count': transcript_count
                }) + "\n"
                
                # 2단계: 미리보기를 위한 SRT 파싱 및 전송
                import re
                entries = re.split(r'\n\s*\n', srt_content.strip())
                
                for i, entry in enumerate(entries):
                    lines = entry.strip().split('\n')
                    if len(lines) >= 3:
                        try:
                            timestamp = lines[1]
                            text = '\n'.join(lines[2:])
                            
                            # 미리보기 전송 (이미 번역된 텍스트)
                            yield json.dumps({
                                'status': 'translating',
                                'preview': {
                                    'timestamp': timestamp,
                                    'original': f"(YouTube 내장 번역: {source_info})",
                                    'translated': text
                                }
                            }) + "\n"
                            
                        except (ValueError, IndexError):
                            continue
                
                # 3단계: 완료 신호
                yield json.dumps({
                    'status': 'completed',
                    'srt_content': srt_content,
                    'video_id': video_id,
                    'count': transcript_count,
                    'source_info': source_info
                }) + "\n"
                
            except Exception as e:
                logger.error(f"YouTube 처리 중 오류: {e}")
                yield json.dumps({'error': f'처리 중 오류가 발생했습니다: {str(e)}'}) + "\n"
                
        except Exception as e:
            logger.error(f"전체 처리 중 오류: {e}")
            yield json.dumps({'error': f'오류가 발생했습니다: {str(e)}'}) + "\n"
    
    return Response(generate(), mimetype='text/plain')

@app.route('/api/languages')
def api_languages():
    """지원하는 언어 목록 반환"""
    # YouTube에서 지원하는 주요 언어들
    languages = {
        'ko': '한국어',
        'en': '영어', 
        'ja': '일본어',
        'zh': '중국어 (간체)',
        'zh-TW': '중국어 (번체)',
        'es': '스페인어',
        'fr': '프랑스어',
        'de': '독일어',
        'it': '이탈리아어',
        'pt': '포르투갈어',
        'ru': '러시아어',
        'ar': '아랍어',
        'hi': '힌디어',
        'th': '태국어',
        'vi': '베트남어',
        'id': '인도네시아어',
        'tr': '터키어'
    }
    return jsonify(languages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)