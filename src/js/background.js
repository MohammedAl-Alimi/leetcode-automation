const displayWelcomePage = () => {
  const url = chrome.runtime.getURL('src/html/welcome.html');
  chrome.tabs.create({ url: url, active: true });
};

const handleMessage = request => {
  if (!request) {
    return;
  }

  if (request.action === 'customCommitMessageUpdated') {
    chrome.storage.local.set({ custom_commit_message: request.message });
  }

  if (request.action === 'tokenSaved') {
    displayWelcomePage();
  }
};

chrome.runtime.onMessage.addListener(handleMessage);
