# BCACTF 1 Write-ups
So this is my first live CTF. Usually I do CTFLearn and picoCTF which always online and doesn't have time limit, but now I did the first live one. I found this CTF by accident because I rarely open CTFtime.org to see any upcoming CTFs. And then there was this CTF, only 2 hours left from the beginning of the competition. Without thinking I registered myself and joined the competition.

There will be several challenges that I would like to make a write-up for because it's interesting enough to explain. It's not going to be all challenges.

# Challenges
## `executable-2`
This challenge is categorized as Binary Exploitation. When you started the file by `./executable-ubuntu`, it will print:
```sh
Welcome to the lottery!
So now we're going to pick a ginormous number!
If it's 1, you win!
Your number is 1804289383!
Try again next time!
```
And it will be the same no matter how many times you started it. This is the place where we change the value of the register to get to the flag.
This is my method by using `gdb` (Use Linux or WSL)
1. `gdb ./executable-ubuntu`
    You will be greeted with `gdb` interface.
2. `disas main`
    It will print a bunch of lines representing the assembly of the binary.
3. You should notice that there is this line that compares a register with `1`
    ```sh
    0x0000000000400691 <+107>:   cmp    $0x1,%ebx
    ```
    `cmp` stands for compare, and `$0x1` is an equivalent of `1`, meanwhile `%ebx` is a register that will be compared with `$0x1`. So what should we do with this? We will change this register value, by stopping the program at that address and manipulate the register content with the one that we want, `$0x1`.
4. `b *0x0000000000400691`
    To set a breakpoint on that address.
5. `r`
    Now run it!
    ```
    Breakpoint 1, 0x0000000000400691 in main ()
    ```
    Now it should print the break.
6. `info registers`
    This will show all the register that exists and its content value.
    ```
    rax            0x1b     27
    rbx            0x6b8b4567       1804289383
    rcx            0x0      0
    rdx            0x0      0
    rsi            0x603260 6304352
    rdi            0x1      1
    rbp            0x7ffffffee040   0x7ffffffee040
    rsp            0x7ffffffece40   0x7ffffffece40
    r8             0x0      0
    r9             0x0      0
    r10            0x0      0
    r11            0x0      0
    r12            0x400530 4195632
    r13            0x7ffffffee120   140737488281888
    r14            0x0      0
    r15            0x0      0
    rip            0x400691 0x400691 <main+107>
    eflags         0x202    [ IF ]
    cs             0x33     51
    ss             0x2b     43
    ds             0x0      0
    es             0x0      0
    fs             0x0      0
    gs             0x0      0
    ```
    Notice the one that we're looking for, `%ebx`. In 32-bit it will be shown as `ebx`, but in 64-bit it will be shown as `rbx`.
7. `set $rbx=1`
    Change the value of the register.
8. `info registers`
    Check if the register already replaced.
9. `next`
    Now it will print the flag :D
    But the flag will be in form of brainfuck language and (those jerks) split it with a newline on each character, so you need a program and an online brainfuck interpreter. You can find the flag at `exc2.txt` and its python newline remover at `exc2.py`.
    `rsqsjv{Arent_executables_fun?_I_think_so_sdkfjhqiweuryiquwerajzncxbvaihqiwueyr}`
    Aaaaand they put it in Caesar Cipher +16. Find the correct format of the flag and you will have the flag.
    `bcactf{Kboxd_ohomedklvoc_pex?_S_drsxu_cy_cnuptrasgoebisaegobktjxmhlfksrasgeoib}`
