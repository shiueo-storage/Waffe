import OpenGL.GL.shaders
import glfw
import math
from OpenGL.GL import *


def gl_set():
    # GL_SETTINGS
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


global program


def shaders():
    global program
    vertex_shader_source = """
    #version 430 core

    void main(void)
    {
        const vec4 vertices[3] = vec4[3](vec4(0.25,-0.25,0.5,1.0),
                                  vec4(0.25, -0.25, 0.5, 1.0),
                                  vec4(0.25,0.25,0.5,1.0));

        gl_Position = vertices[gl_VertexID];
    }
    """

    fragment_shader_source = """
    #version 430 core
    out vec4 color;
    void main(void)
    {
        color = vec4(0.0, 0.8, 1.0, 1.0);
    }
    """
    vertex_shader = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vertex_shader, "1", vertex_shader_source, None)
    glCompileShader(vertex_shader)

    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fragment_shader, "1", fragment_shader_source, None)
    glCompileShader(fragment_shader)

    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)
    print("program!", program)

    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)


def render():
    glClearBufferfv(GL_COLOR, 0, (0, 0, 0.2, 1))
    glUseProgram(program)
    glDrawArrays(GL_TRIANGLES, 0, 3)
