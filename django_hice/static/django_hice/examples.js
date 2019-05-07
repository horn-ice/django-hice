function example1 () {
  ace.edit("id_editor").setValue("// This function definition defines the invariant to be inferred\nfunction {:existential true} my_inv(ab : bool, a#b : bool, #ab : bool, #a#b : bool) : bool;\n\nprocedure main()\n{\n\tvar a, b, c : bool;\n\tassume a != b;\n\n\twhile (*)\n\t// Also try Houdini and decision trees!\n\tinvariant my_inv(a ==> b, a ==> !b, !a ==> b, !a ==> !b);\n\t{\n\t\tc := a;\n\t\ta := !b;\n\t\tb := !c;\n\t}\n\n\tassert a != b;\n}", 1);
  buttons_filter = $('input:radio[name=inference_method][value=SO]').click();
}

function example2 () {
  ace.edit("id_editor").setValue("// This function definition defines the invariant to be inferred\nfunction {:existential true} my_inv (x : int) : bool;\n\nprocedure main()\n{\n\tvar x : int;\n\tx := 0;\n\n\twhile (x < 5)\n\tinvariant my_inv(x);\n\t{\n\t\tx := x + 1;\n\t}\n\n\tassert x == 5;\n}", 1);
  buttons_filter = $('input:radio[name=inference_method][value=DT]').click();
}