@echo off
echo ȫ��ͼת6��ͼ����
echo.

IF "%~1" == "" GOTO ERROR
IF NOT EXIST "%~1" GOTO ERROR

FOR %%V in (%*) do "%~dp0\ktransform" -config=convertdroplets.config "%%~V"

GOTO DONE

:ERROR
echo.
echo ʹ��˵��:
echo.   ��Ҫ˫���򿪣���ʹ��ͼƬ�Ϸš�
echo - ������ȫ��ͼ���Ϸ���BATͼ�꣬
echo   �Ϳ��Էֳ�6������ͼƬ.
echo.
echo.  ����ר��
echo.  QQ��10543884


:DONE
echo.
pause
