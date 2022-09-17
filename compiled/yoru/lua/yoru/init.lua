local M = {}
local theme = require('yoru.theme')

M.setup = function()
  vim.cmd('hi clear')

  vim.o.background = 'dark'
  if vim.fn.exists('syntax_on') then
    vim.cmd('syntax reset')
  end

  vim.o.termguicolors = true
  vim.g.colors_name = 'yoru'

  theme.set_highlights()
end

return M