import shutil
import subprocess
import importlib

repo_url = "git@github.com:shensg/packaging_notice.git"
packaging_dist = "packaging_notice/dist/notice-0.0.1-py3-none-any.whl"
packaging_path = "packaging_notice"

if __name__ == '__main__':
    module = importlib.import_module("flask")
    app = module.Flask(__name__)


    @app.route('/', methods=['GET'])
    def get():
        print("return success")
        return {"code": 0, "data": "66666", "msg": "success"}


    @app.route('/notice', methods=['GET'])
    def notice():
        print("clone external code")
        subprocess.run(['git', 'clone', repo_url])
        subprocess.run(['pip', 'install', '--force-reinstall', packaging_dist])
        shutil.rmtree(packaging_path)
        try:
            from notice import fs_notice
        except EOFError as e:
            print(e)
        image = "img_v3_0296_533eaea3-47d1-48dc-a5e6-7e315214e05g"
        title = "通知测试"
        content = "我们的祖国是花园\n花园的花朵真鲜艳\n阳光和暖的照耀着我们\n每个的脸上的笑开颜！！！！\n"
        webhook = "d45a291c-b3b8-4058-880f-52c87da38855"
        fs_notice.fs_notice(image, title, content, webhook)
        # fs_notice(image, title, content, webhook)
        return {"code": 0, "data": "Send notice success", "msg": "success"}


    app.run(host='0.0.0.0', port=5000, debug=True)
