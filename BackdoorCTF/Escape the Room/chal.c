void _init()
{
    if (__gmon_start__ != 0)
    {
        __gmon_start__();
    }
}

int sub_401020()
{
    int var_8 = data_404008;
    /* jump -> data_404010 */
}

int sub_401030()
{
    int var_8 = 0;
    /* tailcall */
    return sub_401020();
}

int sub_401040()
{
    int var_8 = 1;
    /* tailcall */
    return sub_401020();
}

int sub_401050()
{
    int var_8 = 2;
    /* tailcall */
    return sub_401020();
}

int sub_401060()
{
    int var_8 = 3;
    /* tailcall */
    return sub_401020();
}

int sub_401070()
{
    int var_8 = 4;
    /* tailcall */
    return sub_401020();
}

int sub_401080()
{
    int var_8 = 5;
    /* tailcall */
    return sub_401020();
}

int sub_401090()
{
    int var_8 = 6;
    /* tailcall */
    return sub_401020();
}

int sub_4010a0()
{
    int var_8 = 7;
    /* tailcall */
    return sub_401020();
}

int sub_4010b0()
{
    int var_8 = 8;
    /* tailcall */
    return sub_401020();
}

int sub_4010c0()
{
    int var_8 = 9;
    /* tailcall */
    return sub_401020();
}

int sub_4010d0()
{
    int var_8 = 0xa;
    /* tailcall */
    return sub_401020();
}

int strncmp(char const* arg1, char const* arg2, uint arg3)
{
    /* tailcall */
    return strncmp(arg1, arg2, arg3);
}

int puts(char const* str)
{
    /* tailcall */
    return puts(str);
}

void __stack_chk_fail() __noreturn
{
    /* tailcall */
    return __stack_chk_fail();
}

int system(char const* line)
{
    /* tailcall */
    return system(line);
}

int printf(char const* format, ...)
{
    /* tailcall */
    return printf();
}

ssize_t read(int fd, void* buf, uint nbytes)
{
    /* tailcall */
    return read(fd, buf, nbytes);
}

void srand(uint x)
{
    /* tailcall */
    return srand(x);
}

time_t time(time_t* arg1)
{
    /* tailcall */
    return time(arg1);
}

int setvbuf(FILE* fp, char* buf, int mode, uint size)
{
    /* tailcall */
    return setvbuf(fp, buf, mode, size);
}

int __isoc99_scanf(char const* format, ...)
{
    /* tailcall */
    return __isoc99_scanf();
}

int rand()
{
    /* tailcall */
    return rand();
}

int _start(int arg1, int arg2, void (* arg3)()) __noreturn
{
    int stack_end_1;
    int stack_end = stack_end_1;
    __libc_start_main(main, __return_addr, &ubp_av, nullptr, nullptr, arg3, &stack_end);
    /* no return */
}

int _dl_relocate_static_pie() __pure
{
    return;
}

void deregister_tm_clones()
{
    return;
}

void register_tm_clones()
{
    return;
}

void __do_global_dtors_aux()
{
    if (completed.0 != 0)
    {
        return;
    }
    deregister_tm_clones();
    completed.0 = 1;
}

void frame_dummy()
{
    /* tailcall */
    return register_tm_clones();
}

int setup()
{
    setvbuf(stdout, nullptr, 2, 0);
    setvbuf(stderr, nullptr, 2, 0);
    return setvbuf(stdin, nullptr, 2, 0);
}

int rand_str(char* arg1, int arg2)
{
    char* var_70 = arg1;
    int var_78 = arg2;
    void* fsbase;
    int rax = *(fsbase + 0x28);
    int var_58;
    __builtin_strncpy(&var_58, "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 0x3f);
    while (true)
    {
        int rax_6 = var_78;
        var_78 = (rax_6 - 1);
        if (rax_6 == 0)
        {
            break;
        }
        int512_t zmm2;
        zmm2 = 0x4f000000;
        float zmm0 = (62f * (rand() / 2.14748365e+09f));
        int var_60_1;
        if (zmm0 >= 9.22337204e+18f)
        {
            var_60_1 = ((truncf((zmm0 - 9.22337204e+18f), arg1)) ^ 0x8000000000000000);
        }
        else
        {
            var_60_1 = (truncf(zmm0, arg1));
        }
        char* rax_5 = var_70;
        var_70 = &rax_5[1];
        *rax_5 = *(var_60_1 + &var_58);
    }
    *var_70 = 0;
    if (rax == *(fsbase + 0x28))
    {
        return (rax - *(fsbase + 0x28));
    }
    __stack_chk_fail();
    /* no return */
}

int main(int argc, char** argv, char** envp)
{
    void* fsbase;
    int rax = *(fsbase + 0x28);
    srand(time(nullptr));
    void var_38;
    rand_str(&var_38, 0x1e);
    puts("Welcome to Escape the R00m !");
    puts("You have only two chances to esc…");
    printf("Enter key : ");
    void buf;
    read(0, &buf, 0x50);
    if (strncmp(&var_38, &buf, 0x1e) != 0)
    {
        printf("%s is not the key, try again !\n", &buf);
    }
    else
    {
        puts("That was a nice escape ... But t…");
    }
    printf("Enter key : ");
    __isoc99_scanf(&data_4020c0, &buf);
    if (strncmp(&var_38, &buf, 0x1e) != 0)
    {
        puts("Wrong, go away !");
    }
    else
    {
        puts("That was a nice escape ... But t…");
    }
    *(fsbase + 0x28);
    if (rax == *(fsbase + 0x28))
    {
        return 0;
    }
    __stack_chk_fail();
    /* no return */
}

int escape()
{
    puts("Sweet !");
    return system("/bin/sh");
}

int _fini() __pure
{
    return;
}