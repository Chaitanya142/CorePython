.section .rodata
	msgP1:
	.string	"HELLO-CPA-36\n" 
	msgP2:
	.string	"WORLD-CPA-36\n" 
.section .data
	a:
	.int	20	
	b:
	.int	10

.section .text
.globl	main
.type	main, @function 

main: 
	pushq	%rbp
	movq	%rsp, %rbp 
	movq	$0, %rax
	movq	$0, %rdx
	movl	a, %eax
	movl	b, %ebx
	cmpq	%rbx, %rax
	jng	else
	movq	$msgP1, %rdi 
	movq	$0, %rax
	call	printf
	jmp	out
else:
	movq	$msgP2, %rdi
	movq	$0, %rax
	call	printf
out: 
	movq	$0, %rax
	call	exit
