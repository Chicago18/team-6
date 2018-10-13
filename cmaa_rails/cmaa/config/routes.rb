Rails.application.routes.draw do
  resources :forms
  get 'welcome/index'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html

  # set root
  root 'welcome#index'
end
