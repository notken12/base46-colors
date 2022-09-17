local M = {}
local theme = require('catppuccin_latte.theme')

M.setup = function()
  vim.cmd('hi clear')

  vim.o.background = 'light'
  if vim.fn.exists('syntax_on') then
    vim.cmd('syntax reset')
  end

  vim.o.termguicolors = true
  vim.g.colors_name = 'catppuccin_latte'

  theme.set_highlights()
end

return M