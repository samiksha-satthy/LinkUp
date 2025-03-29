<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
      <div class="main-left">
        <div class="p-12 bg-white border border-gray-200 rounded-lg">
          <h1 class="mb-6 text-2xl">Log In</h1>
          <p class="mb-6 text-gray-500">this is to log into the application</p>
          <p class="font-bold">
            don't have an account?
            <RouterLink to="/signup" class="underline">Click here</RouterLink> to Sign Up!
          </p>
        </div>
      </div>
  
      <div class="main-right">
        <div class="p-12 bg-white border border-gray-200 rounded-lg">
          <form class="space-y-6">
  
              <div>
                  <label>Email</label><br>
                  <input type="email" placeholder="Enter your email" class="w-full py-4 p-2 border border-gray-300 rounded-md" required>
              </div>
  
              <div>
                  <label>Password</label>
                  <input type="password" placeholder="Enter your password" class="w-full py-4 p-2 border border-gray-300 rounded-md" required>
              </div>
  
              <div>
                  <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Log In</button>
              </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  