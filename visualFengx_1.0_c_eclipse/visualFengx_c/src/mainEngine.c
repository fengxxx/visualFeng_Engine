#include <windows.h>
#include <gl/gl.h>
#include <gl/glut.h>
//#include <GL/glaux.h>

float fengx=0;
LRESULT CALLBACK WindowProc(HWND, UINT, WPARAM, LPARAM);
void EnableOpenGL(HWND hwnd, HDC*, HGLRC*);
void DisableOpenGL(HWND, HDC, HGLRC);


int WINAPI WinMain(HINSTANCE hInstance,
                   HINSTANCE hPrevInstance,
                   LPSTR lpCmdLine,
                   int nCmdShow)
{
    WNDCLASSEX wcex;
    HWND hwnd;
    HDC hDC;
    HGLRC hRC;
    MSG msg;
    BOOL bQuit = FALSE;
    float theta = 0.0f;

    /* register window class */
    wcex.cbSize = sizeof(WNDCLASSEX);
    wcex.style = CS_OWNDC;
    wcex.lpfnWndProc = WindowProc;
    wcex.cbClsExtra = 0;
    wcex.cbWndExtra = 0;
    wcex.hInstance = hInstance;
    wcex.hIcon = LoadIcon(NULL, IDI_WINLOGO);
    wcex.hCursor = LoadCursor(NULL, IDC_CROSS);
    wcex.hbrBackground = (HBRUSH)GetStockObject(BLACK_BRUSH);
    wcex.lpszMenuName = "sss";
    wcex.lpszClassName = "visualFeng";
    wcex.hIconSm =LoadIcon(NULL, IDI_WINLOGO);


    if (!RegisterClassEx(&wcex))
        return 0;

    /* create main window */
    hwnd = CreateWindowEx(0,
                          "visualFeng",
                          "visualFeng_v1.0",
                          WS_OVERLAPPEDWINDOW,
                          CW_USEDEFAULT,
                          CW_USEDEFAULT,
                          800,
                          800,
                          NULL,
                          NULL,
                          hInstance,
                          NULL);

    ShowWindow(hwnd, nCmdShow);

    /* enable OpenGL for the window */
    EnableOpenGL(hwnd, &hDC, &hRC);

    /* program main loop */
    while (!bQuit)
    {
        /* check for messages */
        if (PeekMessage(&msg, NULL, 0, 0, PM_REMOVE))
        {
            /* handle or dispatch messages */
            if (msg.message == WM_QUIT)
            {
                bQuit = TRUE;
            }
            else
            {
                TranslateMessage(&msg);
                DispatchMessage(&msg);
            }
        }
        else
        {
            /* OpenGL animation code goes here */

            glClearColor(0.2f, 0.2f, 0.2f, 0.2f);
            glShadeModel(GL_FLAT);
            glShadeModel(GL_SMOOTH);
            glClear(GL_COLOR_BUFFER_BIT);
            glMatrixMode(GL_PROJECTION);
            glLoadIdentity();
            GLfloat lightIntensity=3.4;

            //-----------------------light
            GLfloat LightAmbient[]= { 0.0f, 0.1f, 0.1f, 1.0f };
            GLfloat LightDiffuse[]=     {lightIntensity,lightIntensity, lightIntensity, 1.0f };
            GLfloat LightPosition[]=    { 0.5f, 0.30f, 0.5f, 1.0f };
            GLfloat Light_Model_Ambient[] = { -1.0f, -1.0f, -1.0f, 1.0f };
            GLfloat LightSpecular[]=    { 1.0f, 1.0f, 1.0f, 1.0f };
            GLfloat MaterialSpecular[] = { 1.0f,1.0f,1.0f,1.0f };


            glLightfv(GL_LIGHT1,GL_SPECULAR, LightSpecular);//光源的反射分量

            glMaterialfv(GL_FRONT,GL_SPECULAR,MaterialSpecular);//材质的反射分量

            glMaterialf(GL_FRONT,GL_SHININESS,128);//后面的值越大，光线越集中

            glLightfv(GL_LIGHT1, GL_AMBIENT, LightAmbient);
            glLightfv(GL_LIGHT1, GL_DIFFUSE, LightDiffuse);
            glLightfv(GL_LIGHT1, GL_POSITION,LightPosition);
            glLightModelfv(GL_LIGHT_MODEL_AMBIENT, Light_Model_Ambient);
            glEnable(GL_LIGHT1);
            glEnable(GL_LIGHTING);
            glEnable(GL_COLOR_MATERIAL);
            //-----------------------light

            glFrustum(-0.1,0.1,-0.1,0.1,0.15,900);
            gluLookAt(1,1,1,0,0.0,0.0,0.0,0,1);
            GLfloat fogColor [4]={0,0.2,0.99,1};
            glEnable(GL_FOG);
            glFogfv(GL_FOG_COLOR,fogColor);

            //------------------------------draw model
            glPushMatrix();
            glRotated(40,0,1,0);
            glBegin(GL_QUADS);
                glColor3f(0.5f,0.5f,0.5f);
                glVertex2f( -0.5f,-0.5f);
                //glColor3f(0.9f,0.0f,0.2f);
                glVertex2f(0.5f,-0.5f);
                //glColor3f(0.2f,0.9f,0.2f);
                glVertex2f(0.5f,0.5f);
                //glColor3f(0.2f,0.0f,0.2f);
                glVertex2f( -0.5f,0.5f);
            glEnd();
            glRotated(80,1,0,0);
            glBegin(GL_QUADS);
                glColor3f(0.5f,0.5f,0.5f);
                glVertex2f( -0.5f,-0.5f);
                //glColor3f(0.9f,0.0f,0.2f);
                glVertex2f(0.5f,-0.5f);
                //glColor3f(0.2f,0.9f,0.2f);
                glVertex2f(0.5f,0.5f);
                glColor3f(0.2f,0.0f,0.2f);
                glVertex2f( -0.5f,0.5f);

            glEnd();
            glPopMatrix();
            grid(1);
            xyz(50);
            //------------------------------draw model
            SwapBuffers(hDC);
            // printf("opengl li  %d\n",fengx);
            theta += 1.0f;
            Sleep (1);



        }
    }

    /* shutdown OpenGL */
    DisableOpenGL(hwnd, hDC, hRC);

    /* destroy the window explicitly */
    DestroyWindow(hwnd);

    return msg.wParam;
}

void grid(float h){

    glBegin(GL_LINES);
    int ix;
    int i;
    for(ix=0;ix<21;ix++){
        for(i=0;i<21;i++){
            glColor3f(0.5f, 0.5f, 0.5f);
            glVertex3f(-0.8f, (float)i * 0.08f - 0.8f,h);
            glVertex3f(0.8f, (float)i * 0.08f - 0.8f, h);
            glVertex3f((float)i * 0.08f - 0.8, 0.8f, h);
            glVertex3f((float)i * 0.08f - 0.8, -0.8f, h);
        }
    }
    glEnd();
}

void xyz(float xyzL){
    glBegin(GL_LINES);
    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex3f(0.0f, 0.0f, -xyzL);
    glColor3f(0.0f, 1.0f, 0.0f);
    glVertex3f(0.0f, 0.0f, xyzL);
    glColor3f(0.0f, 1.0f, 0.0f);
    glVertex3f(xyzL, 0.0f, 0.0f);
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex3f(-xyzL, 0.0f, 0.0f);
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex3f(0.0f, -xyzL, 0.0f);
    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex3f(0.0f, xyzL, 0.0f);
    glEnd();

}
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
        case WM_CLOSE:
            PostQuitMessage(0);
        break;

        case WM_DESTROY:
            return 0;

        case WM_KEYDOWN:
        {
            switch (wParam)
            {
                case VK_ESCAPE:
                    PostQuitMessage(0);
                break;
            }
        }
        break;

        default:
            return DefWindowProc(hwnd, uMsg, wParam, lParam);
    }

    return 0;
}
void cCube(float cx,float cy,float cz,float sx,float sy,float sz){

    glBegin(GL_QUADS);

    glColor3f(0.0f,1.0f,0.0f);
    glVertex3f( 1.0f*cx+sx, 1.0f*cy+sy,-1.0f*cz+sz);
    glVertex3f(-1.0f*cx+sx, 1.0f*cy+sy,-1.0f*cz+sz);
    glVertex3f(-1.0f*cx+sx, 1.0f*cy+sy, 1.0f*cz+sz);
    glVertex3f( 1.0f*cx+sx, 1.0f*cy+sy, 1.0f*cz+sz);

    glColor3f(1.0f,0.5f,0.0f);
    glVertex3f( 1.0f*cx+sx,-1.0f*cy+sy, 1.0f*cz+sz);
    glVertex3f(-1.0f*cx+sx,-1.0f*cy+sy, 1.0f*cz+sz);
    glVertex3f(-1.0f*cx+sx,-1.0f*cy+sy,-1.0f*cz+sz);
    glVertex3f( 1.0f*cx+sx,-1.0f*cy+sy,-1.0f*cz+sz);

    glColor3f(1.0f,0.0f,0.0f);
    glVertex3f( 1.0f*cx+sx, 1.0f*cy+sy, 1.0f*cz+sz);
    glVertex3f(-1.0f*cx+sx, 1.0f*cy+sy, 1.0f*cz+sz);
    glVertex3f(-1.0f*cx+sx,-1.0f*cy+sy, 1.0f*cz+sz);
    glVertex3f( 1.0f*cx+sx,-1.0f*cy+sy, 1.0f*cz+sz);

    glColor3f(1.0f,1.0f,0.0f);
    glVertex3f( 1.0f*cx+sx,-1.0f*cy+sy,-1.0f*cz+sz);
    glVertex3f(-1.0f*cx+sx,-1.0f*cy+sy,-1.0f*cz+sz);
    glVertex3f(-1.0f*cx+sx, 1.0f*cy+sy,-1.0f*cz+sz);
    glVertex3f( 1.0f*cx+sx, 1.0f*cy+sy,-1.0f*cz+sz);

    glColor3f(0.0f,0.0f,1.0f);
    glVertex3f(-1.0f*cx+sx, 1.0f*cy+sy, 1.0f*cz+sz);
    glVertex3f(-1.0f*cx+sx, 1.0f*cy+sy,-1.0f*cz+sz);
    glVertex3f(-1.0f*cx+sx,-1.0f*cy+sy,-1.0f*cz+sz);
    glVertex3f(-1.0f*cx+sx,-1.0f*cy+sy, 1.0f*cz+sz);

    glColor3f(1.0f,0.0f,1.0f);
    glVertex3f( 1.0f*cx+sx, 1.0f*cy+sy,-1.0f*cz+sz);
    glVertex3f( 1.0f*cx+sx, 1.0f*cy+sy, 1.0f*cz+sz);
    glVertex3f( 1.0f*cx+sx,-1.0f*cy+sy, 1.0f*cz+sz);
    glVertex3f( 1.0f*cx+sx,-1.0f*cy+sy,-1.0f*cz+sz);
    glEnd();


}
void EnableOpenGL(HWND hwnd, HDC* hDC, HGLRC* hRC)
{
    PIXELFORMATDESCRIPTOR pfd;

    int iFormat;

    /* get the device context (DC) */
    *hDC = GetDC(hwnd);

    /* set the pixel format for the DC */
    ZeroMemory(&pfd, sizeof(pfd));

    pfd.nSize = sizeof(pfd);
    pfd.nVersion = 1;
    pfd.dwFlags = PFD_DRAW_TO_WINDOW |
                  PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER;
    pfd.iPixelType = PFD_TYPE_RGBA;
    pfd.cColorBits = 24;
    pfd.cDepthBits = 16;
    pfd.iLayerType = PFD_MAIN_PLANE;

    iFormat = ChoosePixelFormat(*hDC, &pfd);

    SetPixelFormat(*hDC, iFormat, &pfd);

    /* create and enable the render context (RC) */
    *hRC = wglCreateContext(*hDC);

    wglMakeCurrent(*hDC, *hRC);
}

void DisableOpenGL (HWND hwnd, HDC hDC, HGLRC hRC)
{
    wglMakeCurrent(NULL, NULL);
    wglDeleteContext(hRC);
    ReleaseDC(hwnd, hDC);
}


