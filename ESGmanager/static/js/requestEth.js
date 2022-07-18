let account;

document.getElementById('connect-button').addEventListener('click', event => {
    let button = event.target;
    ethereum.request({method: 'eth_requestAccounts'}).then(accounts => {
        account = accounts[0];
        console.log(account);
        button.textContent = 'Connected!';
        button.style.display = 'none';
        const connectedContainer = document.querySelector('.connected-container');
        const sendButton = document.querySelector('#send-button');
        const isConnected = connectedContainer.querySelector('.isConnected');
        const address = connectedContainer.querySelector('.address');
        sendButton.removeAttribute('hidden');
        isConnected.innerText = 'Connected!';
        address.innerText = `wallet address: ${account}`;

        ethereum.request({method: 'eth_getBalance', params: [account, 'latest']}).then(result => {
            console.log(result);
            let wei = parseInt(result, 16);
            let balance = wei / (10 ** 18);
            console.log(balance + " ETH");
            const balanceDiv = connectedContainer.querySelector('.balance');
            balanceDiv.innerText = `balance: ${balance} (ETH)`;
        });
    });
});


document.getElementById('send-button').addEventListener('click', event => {
    let transactionParam = {
        to: account,
        from: account,
        value: '0x38D7EA4C68000'
    };

    ethereum
        .request({method: 'eth_sendTransaction', params: [transactionParam]})
        .then(txhash => {
            console.log(txhash);
            checkTransactionConfirmation(txhash).then(r => alert(r));
        })
        .catch((error) => {
            console.error(error);
        });
});


function checkTransactionConfirmation(txhash) {
    let checkTransactionLoop = () => {
        return ethereum.request({method: 'eth_getTransactionReceipt', params: [txhash]}).then(r => {
            if (r != null) return 'confirmed';
            else return checkTransactionLoop();
        });
    };

    return checkTransactionLoop();
}

ethereum.on('accountsChanged', (accounts) => {
    console.log(accounts);

    ethereum.request({method: 'eth_requestAccounts'}).then(accounts => {
        account = accounts[0];
        console.log(account);
        const connectedContainer = document.querySelector('.connected-container');
        const isConnected = connectedContainer.querySelector('.isConnected');
        const address = connectedContainer.querySelector('.address');
        isConnected.innerText = 'Connected!';
        address.innerText = `wallet address: ${account}`;

        ethereum.request({method: 'eth_getBalance', params: [account, 'latest']}).then(result => {
            console.log(result);
            let wei = parseInt(result, 16);
            let balance = wei / (10 ** 18);
            console.log(balance + " ETH");
            const balanceDiv = connectedContainer.querySelector('.balance');
            balanceDiv.innerText = `balance: ${balance}`;
        });
    });
});

ethereum.on('chainChanged', (_chainId) => window.location.reload());
