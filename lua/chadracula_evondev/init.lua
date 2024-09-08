local M = {}
local theme = require('chadracula_evondev.theme')

M.setup = function()
  vim.cmd('hi clear')

  vim.o.background = 'dark'
  if vim.fn.exists('syntax_on') then
    vim.cmd('syntax reset')
  end

  vim.o.termguicolors = true
  vim.g.colors_name = 'chadracula_evondev'

  theme.set_highlights()
end

return M
