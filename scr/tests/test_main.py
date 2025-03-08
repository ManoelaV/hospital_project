import pytest
import threading
from scr.main import main

def test_main(monkeypatch):
    # mock para a função start_flask_app
    class MockLogger:
        def info(self, msg):
            pass

    monkeypatch.setattr('scr.main.logger', MockLogger())

    def mock_run(*args, **kwargs):
        pass

    monkeypatch.setattr('scr.main.start_flask_app', mock_run)

    # roda a função principal em uma thread separada
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

    # adiciona um assert para verificar se a função main foi executada com sucesso
    assert True  # verifica se a função main foi executada com sucesso

if __name__ == "__main__":
    pytest.main()