function M = label2matrix(label, size)

I = eye(size);
M = I(:, label);

endfunction