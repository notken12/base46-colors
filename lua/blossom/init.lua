local M = {}
local theme = require('blossom.theme')

M.setup = function()
  vim.cmd('hi clear')

  vim.o.background = 'light'
  if vim.fn.exists('syntax_on') then
    vim.cmd('syntax reset')
  end

  vim.o.termguicolors = true
  vim.g.colors_name = 'blossom'

  theme.set_highlights()
end

return M